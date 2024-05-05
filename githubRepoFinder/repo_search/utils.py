import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Function to search repositories on GitHub using the provided query
def search_repositories(query):

    # GitHub API URL for searching repositories
    url = 'https://api.github.com/search/repositories'
    
    # Set authorization headers with GitHub token
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} 
    
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
