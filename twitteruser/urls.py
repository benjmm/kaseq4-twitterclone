from django.urls import path

from twitteruser import views

urlpatterns = [
    path('user/<int:id>/', views.UserView, name='user'),
]
