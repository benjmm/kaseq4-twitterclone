from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import (LoginForm)


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home')))
                # return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'form.html', {'form': form})


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
