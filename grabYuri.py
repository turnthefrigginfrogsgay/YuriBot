import requests
import json
from secrets import useragent


def find_yuri_image():
    base_url = "https://safebooru.donmai.us"
    while True:
        print("Trying to find a yuri image...")
        headers = {'User-Agent': useragent}
        response = requests.get(f"{base_url}/posts.json?tags=order%3Arandom+yuri&limit=1", headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch yuri image: {response.status_code}")
            continue
        responseJson = json.loads(response.content)
        selectedYuri = responseJson[0]

        image_url = selectedYuri['file_url']
        post_id = selectedYuri['id']
        post_tags = selectedYuri['tag_string']
        image_source = selectedYuri['source']

        
        if image_url and post_id and post_tags and image_source:
            print("Yuri image found!")
            
            full_link = f"{base_url}/post/{post_id}"
            image_response = requests.head(image_url, headers=headers)
            print(f"Full link: {full_link}")
            print(f"Image URL: {image_url}")
            print(f"Image URL response: {image_response.status_code}")
            if image_response.status_code == 200:
                print(f"Image URL: {image_url}")
                return image_url, full_link, post_tags, image_source
            
