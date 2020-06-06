from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet


def IndexView(request):
    html = 'index.html'
    tweets = Tweet.objects.all().order_by('-date')[:10]
    return render(request, html, {'tweets': tweets})


@ login_required
def HomeView(request):
    html = 'home.html'
    user = request.user
    following_ids = user.following.values_list('id', flat=True)
    author_tweets = Tweet.objects.filter(author=user)
    following_tweets = Tweet.objects.filter(author__in=following_ids)
    tweets = author_tweets | following_tweets
    recent_tweets = tweets.distinct().order_by('-date')[:10]
    return render(request, html, {'user': user, 'tweets': recent_tweets})
