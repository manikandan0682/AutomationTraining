import requests

# Define headers
headers = {
    'User-Agent': 'Python API Lab Client',
    'Accept': 'application/json'
}

# Make request with headers
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts/1',
    headers=headers
)

print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Data: {response.json()}")