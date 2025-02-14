from django.shortcuts import render



def index(request):
    
    template_data = {}
    
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')