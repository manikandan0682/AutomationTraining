import requests

# API Key in Headers
headers = {
    'X-API-Key': 'my-api-key-123'
}
response = requests.get(
    'https://httpbin.org/headers',
    headers=headers
)
print("Headers Response:", response.json())