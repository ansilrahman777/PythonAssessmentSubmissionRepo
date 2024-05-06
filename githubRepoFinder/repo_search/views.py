from django.shortcuts import render
from .utils import search_repositories, get_repository_details
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        
        # Pagination
        paginator = Paginator(repositories, 10)  # Show 10 repositories per page
        page = request.GET.get('page')
        try:
            repositories = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            repositories = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            repositories = paginator.page(paginator.num_pages)
        
        # Render the results.html template with the repositories, query, and pagination
        return render(request, 'results.html', {'repositories': repositories, 'query': query})
    else:
        # Render the home.html template if there is no query
        return render(request, 'home.html')

def repository_details(request, repository_id):
    # Get details of the repository by its ID
    repository = get_repository_details(repository_id)
    
    # Render the repository_details.html template with the repository details
    return render(request, 'repos_details.html', {'repository': repository})
