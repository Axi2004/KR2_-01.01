from django import forms
from .models import BookIssue, Book


class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ('books', 'student', 'issue_date')


from .forms import BookIssueForm

def issue_book(request):
    if request.method == 'POST':
        form = BookIssueForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = BookIssueForm()
        return render(request, 'issue_book.html', {'form': form})