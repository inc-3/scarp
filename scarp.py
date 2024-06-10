import requests
import json
import re
import sys

#--> Input Cookies Function
def input_cookies():
    return input('Input Cookies: ')

#--> Input Post ID Function
def input_post_id():
    return input('Input Post ID: ')

#--> PostReactions Method
def PostReactions(self, post_url, result):
    # Get cookies from input
    self.cookie = input_cookies()
    
    r = requests.Session()
    req = r.get(post_url, headers=HeadersGet(), cookies={'cookie': self.cookie}, allow_redirects=True).content
    
    # Perform the regular expression search
    post_id_match = re.search('"fb://(\d+)"', str(req))
    
    # Check if a match was found
    if post_id_match:
        # Access the group if a match was found
        post_id = post_id_match.group(1)
        
        # Get post ID from input
        # post_id = input_post_id()
        
        # Construct the GraphQL query to fetch post reactions
        query = '''
        {
          node(id: "''' + post_id + '''") {
            id
            reactions(first: 100) {
              nodes {
                id
              }
            }
          }
        }
        '''
        
        # Send the GraphQL request
        response = r.post('https://www.facebook.com/api/graphql/', data={'fb_api_req_friendly_name': 'SinglePostReactions', 'variables': json.dumps({}), 'doc_id': '3560935007346409', 'query': query}, headers=HeadersPost(), cookies={'cookie': self.cookie}).json()
        
        # Extract user IDs from the response
        reactions = response['data']['node']['reactions']['nodes']
        for reaction in reactions:
            user_id = reaction['id']
            result.append(user_id)
        
        print('\rSedang Dump %s ID' % str(len(result)), end='')
        sys.stdout.flush()
    else:
        print("No post ID found in the response.")
