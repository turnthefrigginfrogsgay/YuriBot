import requests
import re


def find_yuri_image():
    base_url = "https://safebooru.donmai.us"
    while True:
        print("Trying to find a yuri image...")
        response = requests.get(f"{base_url}/posts?tags=order%3Arandom+yuri")
        if response.status_code != 200:
            print(f"Failed to fetch yuri image: {response.status_code}")
            continue
        
        image_match = re.search(r'srcset="(https://cdn\.donmai\.us/180x180/[^"]+\.jpg)', response.text)
        link_match = re.search(r'<a class="post-preview-link" draggable="false" href="(/posts/[^"]+)', response.text)
        
        if image_match and link_match:
            print("Yuri image found!")
            image_url = re.sub(r'\.jpg .*', '.jpg', image_match.group(1).replace("180x180", "original"))
            
            image_response = requests.head(image_url)
            print(f"Full link: {full_link}")
            print(f"Image URL: {image_url}")
            print(f"Image URL response: {image_response.status_code}")
            if image_response.status_code == 200:
                print(f"Image URL: {image_url}")
                return image_url, full_link
            
