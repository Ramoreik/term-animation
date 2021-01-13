import os
import sys
import time

frames = os.listdir('ascii_frames')
print(frames)
print("Starting vid.")
time.sleep(1)
frames.sort()
for frame in frames:
    time.sleep(0.05)
    content = open('ascii_frames/'+frame, 'r').read()
    sys.stdout.write("\r" + content)
    sys.stdout.flush()


