from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.models import Tweet
from .forms import TwitterUserCreationForm


# @ login_required
def UserView(request, id):
    html = "user.html"
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'tweets': tweets})

# https://stackoverflow.com/questions/3222549/
# how-to-automatically-login-a-user-after-registration-in-django


def RegisterView(request):
    html = "form.html"
    if request.method == 'POST':
        form = TwitterUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(
            #     request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))

    form = TwitterUserCreationForm()

    return render(request, html, {'form': form})


@login_required
def FollowView(request, id):
    request.user.following.add(TwitterUser.objects.get(id=id))
    return HttpResponseRedirect(reverse('home'))


@login_required
def UnfollowView(request, id):
    request.user.following.remove(TwitterUser.objects.get(id=id))
    return HttpResponseRedirect(reverse('home'))
