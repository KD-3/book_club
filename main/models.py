from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=32, blank=False, default='book')
    image = models.ImageField(upload_to='book-images', blank=True, default='image.jpg')
    file = models.FileField(upload_to='book-files')

    def __str__(self):
        return self.name


class BookOfTheMonth(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(max_length=100, blank=False)
    active = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.CharField(max_length=32, blank=False, default='name')
    image = models.ImageField(upload_to='book-images', blank=True, default='image.jpg')
    position = models.CharField(max_length=32, blank=False, default='position')

    def __str__(self):
        return self.name
