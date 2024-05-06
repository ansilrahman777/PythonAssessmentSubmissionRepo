from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .utils import search_repositories, get_repository_details
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Repository

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
    
    # If repository details are found
    if repository:
        # Save repository details to the database
        repo_obj, created = Repository.objects.get_or_create(
            name=repository['name'],
            owner=repository['owner']['login'],
            description=repository['description'],
            html_url=repository['html_url'],
            stargazers_count=repository['stargazers_count'],
            watchers_count=repository['watchers_count'],
            forks_count=repository['forks_count'],
        )
        # Check if the repository was newly created or already exists
        if created:
            message = "Repository details saved to the database."
            print("Repository details saved to the database.")
        else:
            message = "Repository details already exist in the database."
            print("Repository details already exist in the database.")
    else:
        message = "Repository details not found."
        print( "Repository details not found.")

    # Render the repository_details.html template with the repository details and message
    return render(request, 'repos_details.html', {'repository': repository, 'message': message})
