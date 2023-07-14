from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', new_books, name='home'),
    path('new_books/', new_books, name='new_books'),
    path('authors/', authors, name='authors'),
    path('genres/', genres, name='genres'),
    path('authors_ad/', authors_ad, name='authors_ad'),
    path('languages/', languages, name='languages'),
    path('conditions/', conditions, name='conditions'),
    path('author/<pk>/', author, name='author'),

    path('books/', BooksView.as_view(), name='books'),
    path('books/<page>', BooksView.as_view(), name='books'),

    path('new_book/', BookCreateView.as_view(), name='new_book'),
    path('book_update/<pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('new_author/', AuthorCreateView.as_view(), name='new_author'),
    path('author_update/<pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author_delete/<pk>/', AuthorDeleteView.as_view(), name='author_delete'),

    path('new_genre/', GenreCreateView.as_view(), name='new_genre'),
    path('genre_update/<pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre_delete/<pk>/', GenreDeleteView.as_view(), name='genre_delete'),

    path('new_language/', LanguageCreateView.as_view(), name='new_language'),
    path('language_update/<pk>/', LanguageUpdateView.as_view(), name='language_update'),
    path('language_delete/<pk>/', LanguageDeleteView.as_view(), name='language_delete'),

    path('search/', search, name='search'),

    path('book/<pk>/', book, name='book'),

    path('cart/', cart, name='cart'),

    path('update_item/', update_item, name='update_item'),
    path('order_done/', order_done, name='order_done'),
    path('booked/', booked, name='booked'),
    path('change_booked/', change_booked, name='change_booked'),

]