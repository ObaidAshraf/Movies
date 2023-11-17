from typing import Any
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie
from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = 'movies/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['data'] = 'Hello to Movies'
        return context

class MoviesView(TemplateView):

    template_name = "movies/movies.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home Page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    
    if title and year:
        movie = Movie(title = title, year = year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    Movie.objects.get(pk=id).delete()
    return HttpResponseRedirect('/movies')