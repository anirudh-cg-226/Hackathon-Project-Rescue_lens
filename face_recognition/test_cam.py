import time
import cv2
import sys
from simple_facerec import SimpleFacerec

print('Starting test_cam.py')

sfr = SimpleFacerec()
try:
    sfr.load_encoding_images('images/')
except Exception as e:
    print('Error loading encodings:', e)
    sys.exit(1)

print('Loaded encodings:', len(sfr.known_face_names))

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    sys.exit(1)

start = time.time()
found_any = False
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to read frame')
            break
        face_locations, face_names = sfr.detect_known_faces(frame)
        if len(face_names) > 0:
            print('Detected names:', face_names)
            found_any = True
            # break after first detection to keep test short
            break
        if time.time() - start > 10:
            print('Timeout: no faces detected in 10s')
            break
        time.sleep(0.05)
finally:
    cap.release()

if found_any:
    print('Test result: success')
    sys.exit(0)
else:
    print('Test result: no detections')
    sys.exit(2)
