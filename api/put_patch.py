import requests

# PUT request (full update)
put_data = {
    'id': 1,
    'title': 'Updated Title',
    'body': 'Updated body content',
    'userId': 1
}

put_response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=put_data
)

print("PUT Response:")
print(f"Status Code: {put_response.status_code}")
print(f"Updated Data: {put_response.json()}\n")

# PATCH request (partial update)
patch_data = {
    'title': 'Only Update Title'
}

patch_response = requests.patch(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=patch_data
)

print("PATCH Response:")
print(f"Status Code: {patch_response.status_code}")
print(f"Updated Data: {patch_response.json()}")