from django.contrib import admin
from django.urls import path
from .views import home_view, base, user_login, register, library


from . import views

urlpatterns = [
    path('home/', home_view, name='home'),
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('', base, name='base'),
    path('library/', library, name='library')
]