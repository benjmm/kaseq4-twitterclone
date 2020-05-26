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
    tweets = Tweet.objects.all().order_by('-date')[:10]
    return render(request, html, {'user': user, 'tweets': tweets})
