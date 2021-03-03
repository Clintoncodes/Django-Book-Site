from .models import Genre
from .forms import SearchBookForm

def navLinks(request):
    genre_links = Genre.objects.all()
    return {'genre_links': genre_links}

def book_search_form(request):
    form = SearchBookForm()
    if request.method == 'POST':
        form = SearchBookForm(request.POST)
        if form.is_valid():
            form.save()
    return{'search_form': form}

    

# # def book_search(request):
# #     form = BookSearchForm(request.GET)
# #     # searchedBooks = Book.objects.filter(book_title__icontains = request.GET.get['searchedBooks'])
# #     if form.is_valid():
# #         form.save()
# #     return {'search_form': form}

#     #  searchedBooks: 'searchedBooks'