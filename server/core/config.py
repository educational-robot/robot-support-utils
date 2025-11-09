from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "/api/v1")
    API_KEY = os.getenv("API_KEY", "_")
    IMAGE_FOLDER_PATH = os.getenv("IMAGE_FOLDER_PATH", "")
    VIDEO_FPS = int(os.getenv("VIDEO_FPS", 30))
    VIDEO_DURATION = int(os.getenv("VIDEO_DURATION", 10))

config = Config()