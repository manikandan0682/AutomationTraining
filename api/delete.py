import requests

# Make DELETE request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

# Check if deletion was successful
if response.status_code == 200:
    print("Resource deleted successfully")
else:
    print(f"Error deleting resource: {response.status_code}")