from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
def base(request, *args, **kwargs):
    return render(request, 'LibraryApp/base.html', {})

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
from .models import Author, Book

# Create your views here.

def home_view(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books' : books,
        'authors' : authors
    }
    return render(request, 'LibraryApp/home.html', context)

