from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import AddTweetForm
from notification.models import Notification
from twitteruser.models import TwitterUser

# @login_required


def TweetView(request, id):
    html = "tweet.html"
    tweet = Tweet.objects.get(id=id)
    return render(request, html, {'tweet': tweet, })


@login_required
def AddTweetView(request):
    html = "form.html"

    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                author=request.user,
                body=data['body'],
            )
            # add @notification detection to define recipient (as list for multiple?)
            recipient = TwitterUser.objects.get(id=1)
            Notification.objects.create(
                recipient=recipient,
                tweet=tweet,
            )
            return HttpResponseRedirect(reverse('tweet', args=(tweet.id,)))

    form = AddTweetForm()

    return render(request, html, {"form": form})
