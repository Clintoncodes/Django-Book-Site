from django.contrib import admin

# Register your models here.
from .models import Book, Genre, BookSearch
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'recommended', 'popular_fiction', 'business')
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug' : ('title',)}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookSearch)