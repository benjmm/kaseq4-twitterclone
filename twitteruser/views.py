from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser


@ login_required
def UserView(request, id):
    html = "user.html"
    user = CustomUser.objects.get(id=id)
    return render(request, html, {'user': user, })
