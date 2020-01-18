from django.db import models
from users.models import CustomUser


# Create your models here.
class Book(models.Model):
    DEFAULT_MEMBER_ID = 1
    name = models.CharField(max_length=32, blank=False, default='book')
    author = models.CharField(max_length=32, default='author')
    book_number = models.CharField(max_length=32, default='Book1')
    issued_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=DEFAULT_MEMBER_ID)
    image = models.ImageField(upload_to='book-images', blank=True, default='image.jpg')
    file = models.FileField(upload_to='book-files', null=True, blank=True)

    def __str__(self):
        return self.name


class BookOfTheMonth(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(max_length=100, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name


class Contact(models.Model):
    name = models.CharField(max_length=32, blank=False, default='name')
    image = models.ImageField(upload_to='book-images', blank=True, default='image.jpg')
    position = models.CharField(max_length=32, blank=False, default='position')

    def __str__(self):
        return self.name
