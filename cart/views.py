from django.shortcuts import render

from movies.models import Movie
from .models import Order, Item
from django.shortcuts import get_object_or_404, redirect
from .utils import calculate_cart_total
from django.contrib.auth.decorators import login_required


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


def clear(request):
    request.session['cart'] = {}
    return redirect('cart:index')


@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids == []):
        return redirect('cart:index')
    
    movies_in_cart = Movie.objects.filter(id__in=movie_ids)
    cart_total = calculate_cart_total(cart, movies_in_cart)
    
    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()
    
    for movie in movies_in_cart:
        item = Item()
        item.movie = movie
        item.price = movie.price 
        item.order = order 
        item.quantity = cart[str(movie.id)]
        item.save()
        
    request.session['cart'] = {}
    ctx = {}
    
    ctx['order_id'] = order.id
    return render(request, 'cart/purchase.html', ctx)