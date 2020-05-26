from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .models import CustomUser
from tweet.models import Tweet


# @ login_required
def UserView(request, id):
    html = "user.html"
    user = CustomUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'tweets': tweets})
