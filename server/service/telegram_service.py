from io import BufferedReader

import requests
from server.core.config import config

def send_telegram_message(message):
    url = config.TELEGRAM_BASE_API + "/sendMessage"
    resource = requests.post(url=url,
                            params={"chat_id": config.TRACKED_CHAT_ID, "text": message, "parse_mode": "Markdown"})
    if resource.json().get("ok") is False:
        resource = requests.post(url=url,
                                 params={"chat_id": config.TRACKED_CHAT_ID, "text": message})
    return resource.json()

def send_photo_message(photo: BufferedReader, caption: str):
    url = config.TELEGRAM_BASE_API + "/sendPhoto"
    files = {'photo': photo}
    data = {'chat_id': config.TRACKED_CHAT_ID, 'caption': caption}

    telegram_response = requests.post(
        url,
        data=data,
        files=files
    )

def send_video_message(video: BufferedReader, caption: str):
    url = config.TELEGRAM_BASE_API + "/sendVideo"
    files = {'video': video}
    data = {'chat_id': config.TRACKED_CHAT_ID, 'caption': caption}

    telegram_response = requests.post(
        url,
        data=data,
        files=files
    )