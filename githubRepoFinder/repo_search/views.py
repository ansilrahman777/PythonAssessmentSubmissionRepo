from django.shortcuts import render
from .utils import search_repositories
from django.core.paginator import Paginator

# View function for rendering the home page
def home(request):
    # Render the home.html template
    return render(request, 'home.html')

# View function for handling search requests
def search(request):
    # Get the search query from the request
    query = request.GET.get('q')
    
    # If there is a query
    if query:
        # Search repositories using the query
        repositories = search_repositories(query)
        
        # Render the results.html template with the repositories and query
        return render(request, 'results.html', {'repositories': repositories, 'query': query})
    else:
        # Render the home.html template if there is no query
        return render(request, 'home.html')
