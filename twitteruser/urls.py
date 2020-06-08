from django.urls import path

from twitteruser import views

urlpatterns = [
    path('user/<int:id>/', views.UserView, name='user'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('follow/<int:id>/', views.FollowView, name='follow'),
    path('unfollow/<int:id>/', views.UnfollowView, name='unfollow'),
]
