from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView),
]
