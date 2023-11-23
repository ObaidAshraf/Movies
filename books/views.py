from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Book

class IndexView(ListView):

    model = Book    
    template_name = 'books/home.html'
    context_object_name = "books"
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.all()[:2]

class BookDetailView(DetailView):

    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['time'] = timezone.now()
        return context

