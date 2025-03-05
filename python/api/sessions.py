import requests

# Create a session
session = requests.Session()

# Set default headers for all requests in this session
session.headers.update({
    'User-Agent': 'Python API Lab Client',
    'Accept': 'application/json'
})

# Make multiple requests using the session
response1 = session.get('https://jsonplaceholder.typicode.com/posts/1')
response2 = session.get('https://jsonplaceholder.typicode.com/posts/2')

# Print results
print("First request:")
print(f"Status Code: {response1.status_code}")
print(f"Data: {response1.json()}\n")

print("Second request:")
print(f"Status Code: {response2.status_code}")
print(f"Data: {response2.json()}")

# Close the session when done
session.close()