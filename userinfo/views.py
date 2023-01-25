from django.shortcuts import render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in!')
        return redirect('index')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
 
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist")
        
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.info(request, 'You Logged in successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Username or Password is incorrect')
    
    return render(request, 'userinfo/login.html')

def logoutUser(request):
    messages.error(request, 'You are logged out!')
    logout(request)
    return redirect('login')