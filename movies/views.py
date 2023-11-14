from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Movie1',
            'year': 2000
        },
        {
            'id': 6,
            'title': 'Movie2',
            'year': 2010
        },
        {
            'id': 7,
            'title': 'Movie3',
            'year': 2020
        },
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")