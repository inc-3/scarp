from requests_html import HTMLSession

def PostReactionsDump(post_url, reaction_type, result_list, session=None, cursor=None):
    # Initialize session if not provided
    if session is None:
        session = HTMLSession()

    # Fetch the fully rendered HTML content
    response = session.get(post_url)
    response.html.render()

    # Extract post ID from the URL
    post_id_match = re.search(r'\/posts\/(\d+)', post_url)
    if post_id_match is None:
        print("Error: Invalid Facebook post URL.")
        return

    post_id = post_id_match.group(1)

    # Extract fb_dtsg value
    fb_dtsg_input = response.html.find('input[name="fb_dtsg"]', first=True)
    if fb_dtsg_input is None:
        print("Error: Could not find input tag with name 'fb_dtsg'.")
        return

    fb_dtsg = fb_dtsg_input.attrs['value']

    # Prepare data for GraphQL request
    data = {
        'doc_id': '481719952165683',
        'fb_dtsg': fb_dtsg,
        'variables': json.dumps({
            'data': {
                'feedback_id': post_id,
                'first': 50,  # Number of reactions to fetch per request
                'after': cursor,
                'include_subsequent': False,
                'display_comments_context_enable_comment': False,
                'display_comments_context_is_ad_preview': False,
                'display_comments_context_is_aggregated_share': False,
                'display_comments_feedback_context': None,
                'feed_location': 'permalink',
                'feedback_source': 22,
                'scale': 1.5,
                'use_default_actor': False,
                'top_level_render_location': 'permalink',
                'stream_initial_count': 0
            }
        })
    }

    # Send GraphQL API request to fetch reactions
    api_response = session.post('https://www.facebook.com/api/graphql/', data=data)
    api_data = api_response.json()

    # Parse response and extract user IDs
    try:
        reactions = api_data['data']['feedback']['reactors']['nodes']
        for reaction in reactions:
            user_id = reaction['id']
            result_list.append(user_id)
    except KeyError:
        print("Failed to extract reactions data.")
        return

    # Check for pagination
    has_next_page = api_data['data']['feedback']['reactors']['page_info']['has_next_page']
    if has_next_page:
        cursor = api_data['data']['feedback']['reactors']['page_info']['end_cursor']
        PostReactionsDump(post_url, reaction_type, result_list, session=session, cursor=cursor)

if __name__ == "__main__":
    # Accept user inputs for post URL and reaction type
    post_url = input("Enter the URL of the Facebook post: ")
    reaction_type = input("Enter the reaction type (e.g., 'LIKE', 'LOVE', 'HAHA', etc.): ").upper()

    result_list = []
    PostReactionsDump(post_url, reaction_type, result_list)
    print("Dumped User IDs:", result_list)
