from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
# from twitteruser.models import TwitterUser


@ login_required
def NotificationsView(request):
    html = 'notifications.html'
    user = request.user
    notification_ids = user.notification_set.values_list('tweet_id', flat=True)
    tweets = Tweet.objects.filter(
        id__in=notification_ids).order_by('-date')[:10]
    # delete current notifications here
    return render(request, html, {'user': user, 'tweets': tweets})
