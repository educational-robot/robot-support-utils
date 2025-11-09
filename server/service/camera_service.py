import os.path
import time
import cv2
from server.core.config import config

def release_camera(cam: cv2.VideoCapture):
    cam.release()
    cv2.destroyAllWindows()

def take_picture() -> str | None:
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        # skip few first frame
        for i in range(10):
            cam.read()
        ret, frame = cam.read()
        if ret:
            path = os.path.join(config.IMAGE_FOLDER_PATH, f"{time.time()}.jpg")
            cv2.imwrite(path, frame)

            release_camera(cam)
            return path

    release_camera(cam)
    return None

def take_video() -> str | None:
    cam = cv2.VideoCapture(0)
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
        return path

    release_camera(cam)
    return None