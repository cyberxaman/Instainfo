import argparse
import json
import requests

def get_instagram_user_data(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        user_data = data['graphql']['user']

        # Get basic user information
        user_id = user_data['id']
        username = user_data['username']
        full_name = user_data['full_name']
        profile_pic_url = user_data['profile_pic_url_hd']
        bio = user_data['biography']
        website = user_data['external_url']
        is_private = user_data['is_private']
        is_verified = user_data['is_verified']

        # Get user's follower and following counts
        followers = user_data['edge_followed_by']['count']
        following = user_data['edge_follow']['count']

        # Get user's posts and media
        media_count = user_data['edge_owner_to_timeline_media']['count']
        media = []
        for post in user_data['edge_owner_to_timeline_media']['edges']:
            media.append({
                'id': post['node']['id'],
                'shortcode': post['node']['shortcode'],
                'display_url': post['node']['display_url'],
                'caption': post['node']['edge_media_to_caption']['edges'][0]['node']['text'],
                'likes': post['node']['edge_media_preview_like']['count'],
                'comments': post['node']['edge_media_to_comment']['count'],
                'timestamp': post['node']['taken_at_timestamp']
            })

        # Combine data into a dictionary and return
        user_info = {
            'user_id': user_id,
            'username': username,
            'full_name': full_name,
            'profile_pic_url': profile_pic_url,
            'bio': bio,
            'website': website,
            'is_private': is_private,
            'is_verified': is_verified,
            'followers': followers,
            'following': following,
            'media_count': media_count,
            'media': media
        }

        return user_info
    else:
        print(f"Could not retrieve data for user {username}")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Instagram user data')
    parser.add_argument('-u', '--username', required=True, help='Instagram username')
    args = parser.parse_args()
    username = args.username

    user_info = get_instagram_user_data(username)

    if user_info:
        print(json.dumps(user_info, indent=4))
