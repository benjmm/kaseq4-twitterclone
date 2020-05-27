from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TwitterUser


class TwitterUserCreationForm(UserCreationForm):
    display_name = forms.CharField(max_length=50)

    class Meta:
        model = TwitterUser
        fields = ('username', 'email', 'display_name')


class TwitterUserChangeForm(UserChangeForm):

    class Meta:
        model = TwitterUser
        fields = ('username', 'email')
