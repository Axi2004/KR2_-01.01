from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Book, Student, IssueRecord
from .forms import IssueBookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def student_books(request, student_id):
    student = Student.objects.get(id=student_id)
    issued_books = IssueRecord.objects.filter(student=student, returned_at__isnull=True)
    return render(request, 'library/student_books.html', {
        'student': student,
        'issued_books': issued_books
    })

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    ) if query else Book.objects.none()
    return render(request, 'library/book_list.html', {'books': books, 'query': query})

def unreturned_books(request):
    unreturned = IssueRecord.objects.filter(returned_at__isnull=True)
    books = [record.book for record in unreturned]
    return render(request, 'library/unreturned_books.html', {'books': books})

def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = IssueBookForm()
    return render(request, 'library/issue_book.html', {'form': form})