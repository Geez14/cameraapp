# from imutils.video import VideoStream
# import imutils
# import os, urllib.request
import cv2
import datetime

# from tensorflow.keras.model


class webcam:

    def __init__(self, fps=30, color=(255, 200, 255)) -> None:
        self.video = cv2.VideoCapture(0)
        self.frametime = webcam.__getframetime(fps)
        self.color = color
        self.font = cv2.FONT_HERSHEY_DUPLEX

    @staticmethod
    def __getframetime(fps) -> int:
        if fps >= 1000 or fps <= 0:
            return 1
        timing = int(1000 / fps)
        return timing

    # bad practice! to handle it use try finally to release()
    def __del__(self) -> None:
        self.video.release()

    def get_frame(self):
        success, frames = self.video.read()

        cv2.waitKey(self.frametime)
        # convert the all image to gray so model is efficient
        # gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # send all the image info to model on !!frames!!

        # add text on photo
        # cv2.putText(frames, "hello", (10,30), self.font, 1, self.color, 3, cv2.LINE_AA)

        # flipping the image
        frame_flip = cv2.flip(frames, 1)
        ret, jpeg = cv2.imencode(".jpg", frame_flip)

        return jpeg.tobytes()
