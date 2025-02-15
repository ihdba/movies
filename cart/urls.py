from django.urls import path

app_name = 'cart'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/add/', views.add, name='add'),
]
