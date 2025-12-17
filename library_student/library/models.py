from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    student_card_number = models.CharField(max_length=50, unique=True, verbose_name="Номер студенческого билета")

    def __str__(self):
        return f"{self.full_name} ({self.student_card_number})"

class Book(models.Model):
    isbn = models.CharField(max_length=17, unique=True, verbose_name="ISBN")
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=200, verbose_name="Автор")
    year = models.PositiveIntegerField(verbose_name="Год издания")

    def __str__(self):
        return f"{self.title} — {self.author}"

    @property
    def is_available(self):
        return not self.issuerecord_set.filter(returned_at__isnull=True).exists()

class IssueRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    issued_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выдачи")
    returned_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата возврата")

    def __str__(self):
        status = "возвращена" if self.returned_at else "выдана"
        return f"{self.book} → {self.student} ({status})"