"""
URL configuration for student_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from student_library import views

urlpatterns = [
    path('books/', views.book_list),
    path('student/<int:student_id>/books/', views.student_books, name='student_books'),
    path('search/', views.book_search, name='book_search'),
    path('not-returned/', views.not_returned_books, name='not_returned' ),
    path('issue-book/', views.issue_book , name='issue_book'),
]
