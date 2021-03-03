from django.shortcuts import render, redirect
from .models import Book, Genre
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    recommended_books = Book.objects.filter(recommended = True)
    top_fictions = Book.objects.filter(popular_fiction = True)
    business_books = Book.objects.filter(business = True)
    return render(request, 'home.html', {'recommended_books': recommended_books,
    'top_fictions': top_fictions, 'business_books':business_books})

def all_books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'all_books.html', {'books':books})

@login_required(login_url = 'login')
def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    book_genre = book.genre.first()
    similar_books = Book.objects.filter(genre__name__startswith = book_genre)
    return render(request, 'book_detail.html', {'book':book, 'similar_books': similar_books})

def preview_book(request, slug):
    book_preview = Book.objects.get(slug = slug)
    return render(request, 'preview_detail.html', {'book_preview':book_preview})

def genre_detail(request, slug):
    genre = Genre.objects.get(slug=slug)
    genre_books = genre.books.all()
    return render(request, 'genre_detail.html', {'genre': genre, 'genre_books': genre_books})

def book_search(request):
    # search_book_name = request.GET.get('name')
    search_book = Book.objects.filter(title__icontains = request.POST.get('name'))
    return render(request, 'book_search.html', {'search_books': search_book})

# def signup(request):
#     form = RegisterForm()
#     if request.method == 'P0ST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     return render(request, 'signup.html', {'signup_form': form})
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'signup.html', {'signup_form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {})

def signout(request):
    logout(request)
    return redirect('home')
