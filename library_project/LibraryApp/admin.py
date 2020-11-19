from django.contrib import admin
from .models import Author, Book, ActiveUsers

from . import models
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(ActiveUsers)
