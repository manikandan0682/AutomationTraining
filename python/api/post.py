import requests

# Data to send in the POST request
new_post = {
    'title': 'My New Post',
    'body': 'This is the content of my post',
    'userId': 1
}

# Make a POST request
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=new_post
)

# Check response
if response.status_code == 201:
    created_post = response.json()
    print("Created post:", created_post)
else:
    print(f"Error: {response.status_code}")