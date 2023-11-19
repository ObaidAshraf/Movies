from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book

class IndexView(TemplateView):
    
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

