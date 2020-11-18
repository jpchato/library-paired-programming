from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    context = {
        'books' : books,
    }
    return render(request, 'LibraryApp/home.html', context)

