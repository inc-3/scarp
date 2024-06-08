import requests

# Replace with your access token and video ID
access_token = 'EAAWJ3kgZBI88BO1GJuaTomLY5j9SwjW2VgVRGxZCq9tN7o6wdZAyapRwZAlBJAocIN4SZB4Ed0gCwZBXyj4bmsVvYoWVDN0hV2Elf3gleIvdZCiKdfC9hlxNka27aaQe197fhZAhqcr61Yxjbhn0XyZAjgjKS6dFPVBZAXjPceLo8ZBOFkSWUZAdMqpXZBHc0a6xOLJV4MFHW6hX7yMH6sOWOww1y9kQNCAwZD'
video_id = '1103359090738517'

url = f'https://graph.facebook.com/v12.0/{video_id}/reactions'
params = {
    'access_token': access_token,
    'limit': 100  # Adjust limit as needed
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if 'data' in data:
        # Print out user IDs and names
        for reaction in data['data']:
            user_id = reaction['id']
            user_name = reaction.get('name', 'No name available')
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
