from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet


@ login_required
def TweetView(request, id):
    html = "tweet.html"
    tweet = Tweet.objects.get(id=id)
    return render(request, html, {'tweet': tweet, })
