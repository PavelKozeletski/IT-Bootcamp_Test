from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('get_books/', views.get_books, name='get_books'),
    path('get_authors/', views.get_authors, name='get_authors'),
    path('input/', views.input_page, name='input_page'),
    path('input_author/', views.input_author, name='input_author'),
]