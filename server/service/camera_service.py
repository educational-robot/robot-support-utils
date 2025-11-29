import os.path
import time
import cv2
import redis

from server.core.config import config
from server.service import telegram_service


def release_camera(cam: cv2.VideoCapture):
    cam.release()
    cv2.destroyAllWindows()

def take_picture() -> str | None:
    print('taking picture...')
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        # skip few first frame
        for i in range(10):
            cam.read()
        ret, frame = cam.read()
        print('ret is ', ret)
        if ret:
            path = os.path.join(config.IMAGE_FOLDER_PATH, f"{time.time()}.jpg")
            print(path)
            cv2.imwrite(path, frame)
            release_camera(cam)

            # call telegram api to send back message
            with open(path, "rb") as f:
                telegram_service.send_photo_message(f, 'Đây là ảnh chụp từ webcam')

            return path

    print('done taking picture...')
    release_camera(cam)
    return None

def take_video() -> str | None:
    print('taking video...')
    cam = cv2.VideoCapture(0)
    print(cam.isOpened())
    if cam.isOpened():
        width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cam.get(cv2.CAP_PROP_FPS))
        duration = config.VIDEO_DURATION
        path = os.path.join(config.IMAGE_FOLDER_PATH, f"{time.time()}.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # (*'MP42')
        out = cv2.VideoWriter(
            path,
            fourcc,
            fps,
            (width, height)
        )

        for i in range(10):
            cam.read()

        print("Bắt đầu quay video...")
        print('fps:', fps)
        start_time = time.time()
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            out.write(frame)
            if time.time() - start_time > duration:
                break

        out.release()
        release_camera(cam)

        # call telegram api to send back message
        with open(path, "rb") as f:
            telegram_service.send_video_message(f, 'Đây là video từ webcam')

        return path

    print('done taking video...')
    release_camera(cam)
    return None

def listen_redis_command():
    r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe(config.REDIS_SUBSCRIBE_CHANNEL)

    print('Listening redis command...')
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(message)
            if message['data'] == 'take_picture':
                take_picture()
            elif message['data'] == 'take_video':
                take_video()

    print('Stop listening redis command...')
