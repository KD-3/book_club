from django.contrib import admin
from .models import Book, BookOfTheMonth, Contact

# Register your models here.
admin.site.register(Book)
admin.site.register(BookOfTheMonth)
admin.site.register(Contact)
