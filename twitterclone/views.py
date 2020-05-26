from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def IndexView(request):
    html = 'index.html'
    return render(request, html)


@ login_required
def HomeView(request):
    html = 'home.html'
    user = request.user
    return render(request, html, {'user': user})
