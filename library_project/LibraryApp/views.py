from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books' : books,
        'authors' : authors
    }
    return render(request, 'LibraryApp/home.html', context)

