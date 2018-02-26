import cv2
import os
import pickle
import time
import redis


rtsp_address=os.environ['RTSP_ADDRESS']
cap = cv2.VideoCapture(rtsp_address)
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

