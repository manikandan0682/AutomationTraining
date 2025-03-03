import requests

# Bearer Token Authentication
headers = {
    'Authorization': 'Bearer my-test-token'
}
response = requests.get(
    'https://httpbin.org/bearer',
    headers=headers
)
print("Bearer Token Response:", response.json())