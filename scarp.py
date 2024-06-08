import requests

# Replace with your actual access token and video ID
access_token = 'EAAVfBqLSsmwBOZC3Qh4WYw1QIZB3H8pJNqCjp4TxPJvrPCAY7H2TEdKh8EwpqHLevZBI93BdpEG5Tg99Q0XCsNpaFiAuZBQGX1VFA5MisOr4J5KX0bbDjZBXi3v8qhHBkqIUuZBs1PKeWKfjUyesPXNKTIeQgDgHGCkZCWCy130OFjjaeLZA0ZAZB0NWHvON7trhu66J5qeEKZAUFdV3XqzMv9XMtN0SYqlgf6tzeSVtH8SYHnaWBde9dP8HZBLkeP86kQZDZD'
video_id = 'YOUR_VIDEO_ID'  # Replace with your video ID

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
