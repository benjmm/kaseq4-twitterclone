from django.shortcuts import render
# from authentication.forms import (LoginForm, AddBugForm)


def index_v(request):
    html = 'index.html'
    return render(request, html)
