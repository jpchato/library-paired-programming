from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Author')
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ActiveUser(models.Model):
    # user = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    # book = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='Book')
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.user.username
