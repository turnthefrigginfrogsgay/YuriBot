import requests
import re


def find_yuri_source(link):
    while True:
        print("Trying to find a yuri source...")
        response = requests.get(link)
        if response.status_code != 200:
            print(f"Failed to fetch yuri source: {response.status_code}")
            return False
        li_match = re.search(r'<li id="post-info-source">(.*?)</li>', response.text, re.DOTALL)
        if not li_match:
            return False
        li_content = li_match.group(1)
        source_match = re.search(r'href="([^"]+)"', li_content)
        
        if source_match:
            print("Yuri source found!")
            source_url = source_match.group(1)
            print(f"Source URL: {source_url}")
            return source_url
        return False
