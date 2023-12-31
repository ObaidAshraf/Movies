from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    isbn = models.CharField(max_length=100)
    count = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return self.title