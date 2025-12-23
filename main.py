from atproto import Client, client_utils
from grabYuri import find_yuri_image
from grabSource import find_yuri_source
from secrets import uname, password
import requests
import tempfile
import os
from apscheduler.schedulers.blocking import BlockingScheduler

client = Client()
client.login(uname, password)

def send_post():
    try:
        image_url, full_link = find_yuri_image()
        image_source = find_yuri_source(full_link)

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            image_data = requests.get(image_url).content
            temp_file.write(image_data)
            temp_file_path = temp_file.name

        with open(temp_file_path, "rb") as file:
            if image_source != False:
                text = client_utils.TextBuilder().text(f"WAITER! WAITER! MORE GIRLS KISSING, PLEASE\n").link('source', image_source).text(" (").link('safebooru', full_link).text(")\n").tag("#yuri","yuri").text(" ").tag("#百合","百合").text(" ").tag("#wlw","wlw").text(" ").tag("#lesbian","lesbian").text("\nI am a bot! If I am misbehaving, contact my maintainer (check bio)\n\nHelp keep yuri bot up! ").link("Buy me a Strawberry!","https://buymeacoffee.com/rosedabun")
            else:
                text = client_utils.TextBuilder().text(f"WAITER! WAITER! MORE GIRLS KISSING, PLEASE\n Could not find original source (").link('safebooru', full_link).text(")\n").tag("#yuri","yuri").text(" ").tag("#百合","百合").text(" ").tag("#wlw","wlw").text(" ").tag("#lesbian","lesbian").text("\nI am a bot! If I am misbehaving, contact my maintainer (check bio)\n\nHelp keep yuri bot up! ").link("Buy me a Strawberry!","https://buymeacoffee.com/rosedabun")
            post = client.send_image(text, file, "girls kissing :3")

        os.remove(temp_file_path)
    except Exception as e:
        print(f"Error: {e}")
        send_post()

if __name__ == "__main__":
    scheduler = BlockingScheduler()

    scheduler.add_job(send_post, "cron", hour="*", minute="0")
    scheduler.start()
