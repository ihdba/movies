from django.urls import path


app_name = 'accounts'

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
