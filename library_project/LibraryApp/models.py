from django.db import models

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

class ActiveUsers(models.Model):
    user = models.CharField(max_length=50)
    book = models.CharField(max_length=50)
    checkout = models.Boolean()
    timestamp = models.DateTimeField()
