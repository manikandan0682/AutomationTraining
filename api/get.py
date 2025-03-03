# Make a GET request to a public API
import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")