import requests
from requests.exceptions import RequestException

def make_api_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting to server: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    
    return None

# Test with valid URL
print("\nTesting valid URL:")
result = make_api_request('https://jsonplaceholder.typicode.com/posts/1')
if result:
    print("Success! Retrieved data:", result)
else:
    print("Failed to retrieve data")

# Test with 404 error
print("\nTesting 404 error:")
result = make_api_request('https://jsonplaceholder.typicode.com/posts/999')
if result:
    print("Success! Retrieved data:", result)
else:
    print("Failed as expected - resource not found")

# Test with invalid URL
print("\nTesting invalid URL:")
result = make_api_request('https://invalid-url-that-does-not-exist.com')
if result:
    print("Success! Retrieved data:", result)
else:
    print("Failed as expected - invalid URL")