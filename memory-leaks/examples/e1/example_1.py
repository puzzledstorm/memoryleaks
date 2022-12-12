import cv2
import numpy as np

class Process:
    def __init__(self):
        self.data = []

    def encode(self, frame):
        frame = cv2.imencode('test.jpg', frame)[1]
        return frame

    def decoce(self, frame):
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        self.data.append(frame.copy())
        return frame

    def crop(self, frame):
        return frame[20:80,120:920]
        

if __name__=="__main__":
    m = Process() # 可以理解为 import Process as m
    for i in range(100):
        frame = np.zeros((8000, 8000))
        encoded = m.encode(frame)
        frame = m.decoce(encoded)
        frame2 = m.crop(frame)