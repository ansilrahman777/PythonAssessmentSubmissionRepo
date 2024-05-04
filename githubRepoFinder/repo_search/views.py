from django.shortcuts import render
from .utils import search_repositories
from django.core.paginator import Paginator


def home(request):

    return render(request, 'home.html')

def search(request):
    query = request.GET.get('q')
    if query:
        repositories = search_repositories(query)
        return render(request, 'results.html', {'repositories': repositories, 'query': query})
    else:
        return render(request, 'search.html')
