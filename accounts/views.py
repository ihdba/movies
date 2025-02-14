from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm


def signup(request):
    ctx = {}
    
    if request.method == 'GET':
        ctx['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html', ctx)

    elif request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home:index')
        else:
            ctx['form'] = form
            return render(request, 'accounts/signup.html', ctx)
