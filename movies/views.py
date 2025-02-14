from django.shortcuts import render

# Dummy data 
# movies = [
#     {
#         'id': 1, 'name': 'Inception', 'price': 12, 
#         'description': 'A mind-bending heist thriller.'
#     },
#     {
#         'id': 2, 'name': 'Avatar', 'price': 13, 
#         'description': 'A journey to a distant world and the battle for resourses.'
#     },
#     {
#         'id': 3, 'name': 'The Dark Knight', 'price': 14, 
#         'description': 'Gothams vigilante faces the Joker.'
#     },
#     {
#         'id': 1, 'name': 'Titanic', 'price': 11, 
#         'description': 'A love story set against the backdrop of the sinking Titanic.'
#     },
# ]

from .models import Movie


def index(request):
    
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    
    ctx = {}
    ctx['movies'] = movies
    return render(request, 'movies/index.html', ctx)


def show(request, id):
    
    ctx = {}
    ctx['movie'] = Movie.objects.get(id=id)
    return render(request, 'movies/show.html', ctx)
    