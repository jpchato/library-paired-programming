from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Author, Book

User = get_user_model()

# Create your views here.
def base(request, *args, **kwargs):
    return render(request, 'base.html', {})

def user_login(request, *args, **kwargs):
    if request.method == 'POST':
        user = authenticate(
        request, 
        username = request.POST['username'],
        password = request.POST['password']
        )
        if user is not None: 
            login(request, user)
            return redirect('home')

    return render(request, 'LibraryApp/login.html', {})

def register(request, *args, **kwargs):
    if request.method == 'POST':
        new_user = User(
        username = request.POST['username'],
        email = request.POST['email']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        return redirect('user_login')

    return render(request, 'LibraryApp/register.html', {})

# @login_required
# def home_view(request, *args, **kwargs):
#     return render(request, 'LibraryApp/home.html', {})

# @login_required
def home_view(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books' : books,
        'authors' : authors
    }
    return render(request, 'LibraryApp/home.html', context)

def library(request):
    
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
            'books' : books,
            'authors' : authors
        }

    if request.method == 'GET':
        
        return render (request, 'LibraryApp/library.html', context)

    elif request.method == 'POST':

        book_title = request.POST['book_title']
        single_book = Book.objects.get(title = book_title)
        print(single_book)
        single_book.checked_out = not single_book.checked_out
        single_book.save()

        return render (request, 'LibraryApp/library.html', context)
    


