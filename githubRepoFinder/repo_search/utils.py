import os
from dotenv import load_dotenv
import requests
from django.conf import settings 



# Function to search repositories on GitHub using the provided query
def search_repositories(query):

    # GitHub API URL for searching repositories
    url = 'https://api.github.com/search/repositories'
    
    # Set authorization headers with GitHub token
    headers = {'Authorization': f'token {settings.GITHUB_TOKEN}'} 
    
    # Define search parameters
    params = {'q': query,'per_page': 500}
    
    try:
        # Make a GET request to GitHub API
        response = requests.get(url, headers=headers, params=params)
        
        # Check for HTTP errors
        response.raise_for_status()  
        
        # Convert response to JSON format
        data = response.json()
        
        # Get repositories from response data
        repositories = data.get('items', [])
        
        return repositories

    except requests.exceptions.RequestException as e:
        # Log and handle request errors
        print("Error:", e)
        return []

def get_repository_details(repository_id):

    url = f'https://api.github.com/repositories/{repository_id}'

    headers = {'Authorization': f'token {GITHUB_TOKEN}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        repository = response.json()
        return repository
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
