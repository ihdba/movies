from django.shortcuts import render

from movies.models import Movie
from django.shortcuts import get_object_or_404, redirect
from .utils import calculate_cart_total


def index(request):
    cart_total = 0
    movies_in_cart =[]
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids != []):
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        cart_total = calculate_cart_total(cart, movies_in_cart)
        
    
    ctx = {}
    
    ctx['movies_in_cart'] = movies_in_cart
    ctx['cart_total'] = cart_total
    
    return render(request, 'cart/index.html', ctx)
    

def add(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart:index')    