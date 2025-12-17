from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('student/<int:student_id>/', views.student_books, name='student_books'),
    path('search/', views.search_books, name='search_books'),
    path('unreturned/', views.unreturned_books, name='unreturned_books'),
    path('issue/', views.issue_book, name='issue_book'),
]