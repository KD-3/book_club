from django.urls import path
from . import views as stores_views

app_name = 'users'

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('mybooks', views.IssueCreateView.as_view(template_name='main/mybooks.html'), name='mybooks'),
    path('mybooks/', stores_views.IssueCreateView, name='mybooks'),
    path('delete_issued/<int:id>', stores_views.IssuedDelete, name='issued_delete'),
]
