#!/bin/bash

# clear screen
clear

banner(){
    echo -e "\033[32;1m"
    echo '

 _____                      _        ___      
(_____)           _        (_)      / __)     
   _   ____   ___| |_  ____ _ ____ | |__ ___  
  | | |  _ \ /___)  _)/ _  | |  _ \|  __) _ \ 
 _| |_| | | |___ | |_( ( | | | | | | | | |_| |
(_____)_| |_(___/ \___)_||_|_|_| |_|_|  \___/ 
                                              
'
    echo -e "\033[33;1m MADE BY CYBERXEAL"
}

# show banner
banner

# Function to get Instagram user data
get_instagram_user_data() {
    username=$1
    url="https://www.instagram.com/${username}/?__a=1"
    response=$(curl -s "${url}")

    if [ $? -eq 0 ]; then
        user_data=$(echo "${response}" | jq -r '.graphql.user')

        # Get basic user information
        user_id=$(echo "${user_data}" | jq -r '.id')
        username=$(echo "${user_data}" | jq -r '.username')
        full_name=$(echo "${user_data}" | jq -r '.full_name')
        profile_pic_url=$(echo "${user_data}" | jq -r '.profile_pic_url_hd')
        bio=$(echo "${user_data}" | jq -r '.biography')
        website=$(echo "${user_data}" | jq -r '.external_url')
        is_private=$(echo "${user_data}" | jq -r '.is_private')
        is_verified=$(echo "${user_data}" | jq -r '.is_verified')

        # Get user's follower and following counts
        followers=$(echo "${user_data}" | jq -r '.edge_followed_by.count')
        following=$(echo "${user_data}" | jq -r '.edge_follow.count')

        # Get user's posts and media
        media_count=$(echo "${user_data}" | jq -r '.edge_owner_to_timeline_media.count')
        media=$(echo "${user_data}" | jq -r '.edge_owner_to_timeline_media.edges | .[] | {id: .node.id, shortcode: .node.shortcode, display_url: .node.display_url, caption: .node.edge_media_to_caption.edges[0].node.text, likes: .node.edge_media_preview_like.count, comments: .node.edge_media_to_comment.count, timestamp: .node.taken_at_timestamp}')

        # Combine data into a dictionary and return
        user_info=$(echo "{}" | jq --arg user_id "${user_id}" --arg username "${username}" --arg full_name "${full_name}" --arg profile_pic_url "${profile_pic_url}" --arg bio "${bio}" --arg website "${website}" --arg is_private "${is_private}" --arg is_verified "${is_verified}" --arg followers "${followers}" --arg following "${following}" --arg media_count "${media_count}" --argjson media "${media}" '. + {user_id: $user_id, username: $username, full_name: $full_name, profile_pic_url: $profile_pic_url, bio: $bio, website: $website, is_private: $is_private, is_verified: $is_verified, followers: $followers, following: $following, media_count: $media_count, media: $media}')

        echo "${user_info}"
    else
        echo "Could not retrieve data for user ${username}"
        exit 1
    fi
}

# Parse command line arguments
while getopts ":u:" opt; do
    case $opt in
        u)
            username=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
    esac
done

# Call function to get user data and print it in JSON format
user_info=$(get_instagram_user_data "${username}")
echo "${user_info}" | jq
