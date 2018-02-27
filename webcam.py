import cv2
import os
import pickle
import time
import redis

ip_camera=os.environ['IP_CAMERA']
cap = cv2.VideoCapture('rtsp://' + ip_camera + ':554/11')
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

