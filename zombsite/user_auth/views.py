from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    return render(request, "authentication/login.html")

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register_user(request):    

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']

        user = User.objects.create_user(username=username, password=password, first_name=first_name)

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('user_auth:show_user')
    else:
        return render(request, 'authentication/register.html')
# Create your views here.
