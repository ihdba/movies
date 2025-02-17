from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomErrorList

from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


def signup(request):
    ctx = {}
    
    if request.method == 'GET':
        ctx['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', ctx)

    elif request.method == 'POST':
        
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            ctx['form'] = form
            return render(request, 'accounts/signup.html', ctx)



def login(request):
    ctx ={}
    if request.method =='GET':
        return render(request, 'accounts/login.html')
    elif request.method =='POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            ctx['error'] = "The username or password is incorrect."
            return render(request, 'accounts/login.html', ctx)
        else:
            auth_login(request, user)
            return redirect('home:index')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home:index')



@login_required
def orders(request):
    ctx = {}
    
    ctx['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html', ctx)
    