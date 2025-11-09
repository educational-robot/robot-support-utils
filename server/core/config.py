from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "/api/v1")
    API_KEY = os.getenv("API_KEY", "_")
    IMAGE_FOLDER_PATH = os.getenv("IMAGE_FOLDER_PATH", "/app/image")
    VIDEO_FPS = int(os.getenv("VIDEO_FPS", 30))
    VIDEO_DURATION = int(os.getenv("VIDEO_DURATION", 10))

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    REDIS_SUBSCRIBE_CHANNEL = os.getenv("REDIS_SUBSCRIBE_CHANNEL", "command")

    TRACKED_CHAT_ID = int(os.getenv("TRACKED_CHAT_ID", 1))
    TELEGRAM_BASE_URL = os.getenv("TELEGRAM_BASE_URL", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    TELEGRAM_BASE_API = TELEGRAM_BASE_URL + BOT_TOKEN

config = Config()