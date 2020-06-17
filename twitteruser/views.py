from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.models import Tweet
from .forms import TwitterUserCreationForm
from django.views.generic import View


def UserView(request, id):
    html = "user.html"
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'tweets': tweets})

# https://stackoverflow.com/questions/3222549/
# how-to-automatically-login-a-user-after-registration-in-django


class RegisterView(View):
    html = "form.html"

    def get(self, request):
        form = TwitterUserCreationForm()
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = TwitterUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
        return render(request, self.html, {'form': form})


@login_required
def FollowView(request, id):
    request.user.following.add(TwitterUser.objects.get(id=id))
    return HttpResponseRedirect(reverse('user', args=(id,)))


@login_required
def UnfollowView(request, id):
    request.user.following.remove(TwitterUser.objects.get(id=id))
    return HttpResponseRedirect(reverse('user', args=(id,)))
