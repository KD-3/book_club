from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import IssueBook
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import IssueCreateForm
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


def IssueCreateView(request):
    books = IssueBook.objects.filter(user=request.user)

    if request.method == 'POST':
        form = IssueCreateForm(request.POST)
        if form.is_valid():
            book = IssueBook()
            book.book = form.cleaned_data.get('book')
            # book.number = form.cleaned_data.get('number')
            book.received = False
            book.user = request.user
            book.save()
            return HttpResponseRedirect("/users/mybooks/")
    else:
        form = IssueCreateForm()
    return render(request, 'frontend_new/my_books.html', {'form': form, 'books': books})


def IssuedDelete(request, id):
    post = get_object_or_404(IssueBook, id=id)
    post.delete()
    return redirect('users:mybooks')
