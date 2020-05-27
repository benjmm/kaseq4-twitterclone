from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from tweet.models import Tweet


# @ login_required
def UserView(request, id):
    html = "user.html"
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'tweets': tweets})
