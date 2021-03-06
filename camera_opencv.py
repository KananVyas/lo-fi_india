import os
import cv2
from base_camera import BaseCamera
import pafy
class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source



    @staticmethod
    def frames():
        url = 'https://www.youtube.com/watch?v=_ZZ6xiBHgbg'
        video = pafy.new(url)
        best  = video.getbest(preftype="mp4")
        camera = cv2.VideoCapture(best.url)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
