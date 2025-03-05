import requests

# Parameters as a dictionary
params = {
    'page': 1,
    'limit': 100,
    'sort': 'desc'
}

# Make GET request with parameters
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params=params
)

# URL with parameters will be printed
print(f"Request URL: {response.url}")
print(f"Results: {response.json()[:2]}")  # Print first 2 results