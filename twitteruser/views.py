from django.shortcuts import render, reverse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.models import Tweet
from .forms import TwitterUserCreationForm


# @ login_required
def UserView(request, id):
    html = "user.html"
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'tweets': tweets})


def RegisterView(request):
    html = "form.html"
    if request.method == 'POST':
        form = TwitterUserCreationForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))

    form = TwitterUserCreationForm()

    return render(request, html, {'form': form})
