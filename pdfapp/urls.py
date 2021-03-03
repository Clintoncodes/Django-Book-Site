from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('books', views.all_books, name = 'all_books'),
    path('genre/<slug:slug>', views.genre_detail, name = 'genre_books'),
    path('book/<slug:slug>', views.book_detail, name = 'book_detail'),
    path('preview/<slug:slug>', views.preview_book, name = 'preview_book'),
    path('book_search', views.book_search, name = 'book_search'),
    path('signup_page', views.signup, name = 'signup'),
    path('login_page', views.login_user, name = 'login'),
    path('logout', views.signout, name = 'signout')
    ]