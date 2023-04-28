import requests

# Define the API endpoint URL
url = "https://api.example.com/customers"

# Define the request headers and parameters
headers = {
    "Authorization": "Bearer <access_token>",
    "Content-Type": "application/json"
}
params = {
    "start_date": "2022-01-01",
    "end_date": "2022-03-31"
}

# Send the GET request to retrieve the data
response = requests.get(url, headers=headers, params=params)

# Check the status code to ensure the request was successful
if response.status_code == 200:
    # Extract the data from the response JSON
    data = response.json()
    # Process the data as needed
    # ...
else:
    # Handle any errors that occurred during the request
    print(f"Error retrieving data: {response.status_code}")
