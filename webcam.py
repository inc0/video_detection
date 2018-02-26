import cv2
import numpy
import socket
from sys import getsizeof
import pickle
import struct
import time
import redis



cap = cv2.VideoCapture('rtsp://192.168.0.107:554/11')
r = redis.StrictRedis(host='redis', port=6379, db=0)
n_frames = 0
start = time.time()
while True:
    _, f = cap.read()
    n_frames += 1
    r.set('img', pickle.dumps(f))
    if n_frames % 10 == 0:
        print(n_frames / (time.time() - start))
        n_frames = 0
        start = time.time()

