from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from book_club import settings

urlpatterns = [
    path('', views.HomePageView.as_view(template_name='frontend_new/index.html'), name='home'),
    path('book-list', views.BookListPageView.as_view(template_name='main/book_list.html'), name='book-list'),
    path('blog', views.BlogPageView.as_view(template_name='main/blog.html'), name='blog'),
    path('contact', views.ContactPageView.as_view(template_name='main/contact.html'), name='contact'),
    path('mybooks', views.MyBooksView.as_view(template_name='main/mybooks.html'), name='mybooks'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
