from django.shortcuts import render, redirect, get_object_or_404


from .models import Movie, Review
from django.contrib.auth.decorators import login_required


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
    
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    ctx = {}
    ctx['movie'] = movie
    ctx['reviews'] = reviews
    return render(request, 'movies/show.html', ctx)
    

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] !='':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie 
        review.user = request.user
        review.save()
        return redirect('movies:show', id=id)
    else:
        return redirect('movies:show', id=id)
        
@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies:show', id=id)
    if request.method =='GET':
        ctx = {}
        ctx['review'] = review
        return render(request, 'movies/edit_review.html', ctx)
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies:show', id=id)
    else:
        return redirect('movies:show', id=id)