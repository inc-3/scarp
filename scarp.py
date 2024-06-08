import os
import requests

# Retrieve access token from environment variable
access_token = os.getenv('EAAWJ3kgZBI88BOwWs0PMd5av5GgcAuZBuEOA92zKpnSQhrm0Iitd3MCk6R5VxfwkhNywxrA9CHsd1L0RE5jQTQ7L4onNtFj8oU8RyxZBAp7ZAXGz9FW7mGbZCXPF76yNTQSZADVqkYSZBbudCW3gnWyZAwSX5VgmyK9Wdesqbwz5yygsEi4XmI4WleCvFHvfUid3ZAqu5dRDIY4Sk4QPcRwZDZD')

if access_token is None:
    print("Error: Access token not found. Please set the 'FACEBOOK_ACCESS_TOKEN' environment variable.")
    exit()

# Replace 'POST_ID' with the ID of the Facebook post you want to retrieve comments from
post_id = '435225199274433'

url = f'https://graph.facebook.com/v12.0/{post_id}/comments'
params = {
    'access_token': access_token,
    'limit': 100  # Adjust limit as needed
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if 'data' in data:
        # Print out user IDs and names
        for comment in data['data']:
            user_id = comment['from']['id']
            user_name = comment['from'].get('name', 'No name available')
            print(f'User ID: {user_id}, Name: {user_name}')
    else:
        print("No 'data' key found in the response.")
        print(data)
else:
    # Print the error details
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    error_response = response.json()
    print(error_response)
    # Additional error handling based on error type and code
    error_message = error_response.get('error', {}).get('message', '')
    error_type = error_response.get('error', {}).get('type', '')
    error_code = error_response.get('error', {}).get('code', '')
    error_subcode = error_response.get('error', {}).get('error_subcode', '')
    print(f"Error Message: {error_message}")
    print(f"Error Type: {error_type}")
    print(f"Error Code: {error_code}")
    print(f"Error Subcode: {error_subcode}")
