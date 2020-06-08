from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Tweet
from .forms import AddTweetForm
from notification.models import Notification
from twitteruser.models import TwitterUser
import re
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


def TweetView(request, id):
    html = "tweet.html"
    tweet = Tweet.objects.get(id=id)
    return render(request, html, {'tweet': tweet, })


class AddTweetView(LoginRequiredMixin, View):

    def get(self, request):
        html = "form.html"
        form = AddTweetForm()
        return render(request, html, {"form": form})

    def post(self, request):
        html = "form.html"
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                author=request.user,
                body=data['body'],
            )
            mentions = re.findall('@\w+', data['body'])
            recipients = {TwitterUser.objects.get(username=mention[1:])
                          for mention in mentions if (mention[1:],)
                          in TwitterUser.objects.values_list('username')}
            for recipient in recipients:
                Notification.objects.create(
                    recipient=recipient,
                    tweet=tweet,
                )
            return HttpResponseRedirect(reverse('tweet', args=(tweet.id,)))
        return render(request, html, {"form": form})
