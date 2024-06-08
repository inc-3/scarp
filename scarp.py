import requests

def get_user_input(prompt):
    """
    Helper function to get user input with a prompt.
    """
    return input(prompt).strip()

# Get access token from user input
access_token = get_user_input("Enter your Facebook access token: ")

# Replace 'POST_ID' with the ID of the Facebook post you want to retrieve comments from
post_id = get_user_input("Enter the ID of the Facebook post: ")

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
