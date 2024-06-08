import requests

# Replace with your access token and video ID
access_token = 'EAAVfBqLSsmwBOZC3Qh4WYw1QIZB3H8pJNqCjp4TxPJvrPCAY7H2TEdKh8EwpqHLevZBI93BdpEG5Tg99Q0XCsNpaFiAuZBQGX1VFA5MisOr4J5KX0bbDjZBXi3v8qhHBkqIUuZBs1PKeWKfjUyesPXNKTIeQgDgHGCkZCWCy130OFjjaeLZA0ZAZB0NWHvON7trhu66J5qeEKZAUFdV3XqzMv9XMtN0SYqlgf6tzeSVtH8SYHnaWBde9dP8HZBLkeP86kQZDZD'
video_id = '774179221564480'

url = f'https://graph.facebook.com/v12.0/{video_id}/reactions'
params = {
    'access_token': access_token,
    'limit': 100  # Adjust limit as needed
}

response = requests.get(url, params=params)
data = response.json()

# Print out user IDs and names
for reaction in data['data']:
    user_id = reaction['id']
    user_name = reaction.get('name', 'No name available')
    print(f'User ID: {user_id}, Name: {user_name}')
