import requests

GITHUB_TOKEN ='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'

def search_repositories(query):

    url = 'https://api.github.com/search/repositories'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} 
    params = {'q': query,'per_page': 500}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() 
        
        data = response.json()
        repositories = data.get('items', [])
        
        return repositories
        
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []
