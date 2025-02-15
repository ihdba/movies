from django.urls import path

app_name = 'movies'


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/review/create/', views.create_review, name='create_review'),
]
