from django.views.generic import TemplateView
from .models import Book, BookOfTheMonth, Contact


class HomePageView(TemplateView):
    template_name = 'frontend_new/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        context['boftm'] = BookOfTheMonth.objects.all()

        return context


class BookListPageView(TemplateView):
    template_name = 'frontend_new/book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BookListPageView, self).get_context_data()
        context['books'] = Book.objects.all()

        return context


class BlogPageView(TemplateView):
    template_name = 'main/blog.html'


class ContactPageView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data()
        context['contacts'] = Contact.objects.all()

        return context


class MyBooksView(TemplateView):
    template_name = 'main/mybooks.html'


class AboutUsView(TemplateView):
    template_name = 'frontend_new/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data()
        context['contacts'] = Contact.objects.all()

        return context
