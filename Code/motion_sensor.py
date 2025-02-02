from gpiozero import MotionSensor
from time import sleep
import os

pir = MotionSensor(21)  # Port 21

print("Waiting for Motion.")

while True:
    if pir.motion_detected:
        print("Motion detected.")
        os.system("libcamera-still -o motion_capture.jpg")
    else: 
        print("No Motion detected")

    sleep(2)