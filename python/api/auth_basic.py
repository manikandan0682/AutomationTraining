import requests

# Basic Authentication
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=('user', 'pass')
)
print("Basic Auth Response:", response.json())