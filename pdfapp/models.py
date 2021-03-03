from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, default = 'dothis')
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='img', null = True, blank = True)
    slug = models.SlugField(max_length = 200)
    summary = models.TextField()
    author = models.CharField(max_length = 100)
    genre = models.ManyToManyField(Genre, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    recommended = models.BooleanField(default=False)
    popular_fiction = models.BooleanField(default=False)
    business = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class BookSearch(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name