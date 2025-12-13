from django.shortcuts import render
from .models import Book, BookIssue


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def student_books(request, student_id):
    books = BookIssue.objects.filter(student_id=student_id, return_date__isnull=False)
    return render(request, 'books/student_books.html', {'books': books})

def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(title__icontains=query)
    return render(request, 'books/book_search.html', {'books': books})

def not_returned_books(request):
    books = Book.objects.filter(return_date__isnull=True)
    return render(request, 'books/not_returned_books.html', {'books': books})
