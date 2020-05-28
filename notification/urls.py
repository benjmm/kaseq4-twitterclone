from django.urls import path

from notification import views

urlpatterns = [
    path('notifications/', views.NotificationsView, name='notifications'),
    path('notify/', views.NotifyView),
]
