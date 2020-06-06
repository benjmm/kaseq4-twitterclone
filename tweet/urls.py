from django.urls import path

from tweet import views

urlpatterns = [
    path('tweet/<int:id>/', views.TweetView, name='tweet'),
    path('addtweet/', views.AddTweetView, name='addtweet'),
]
