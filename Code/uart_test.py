import serial
import RPi.GPIO as GPIO
import time
from picamera import PiCamera

# Set up serial communication with Free Wili
ser = serial.Serial('/dev/serial0', 115200, timeout=1)

# Set a sound threshold (this will depend on your Free Wili's microphone readings)
SOUND_THRESHOLD = 50  # Adjust based on what is considered a loud enough sound

# Set up the PiCamera
camera = PiCamera()

def capture_image():
    """Function to capture an image when sound is detected."""
    print("Sound detected! Capturing image...")
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Timestamp for unique file name
    camera.capture(f'/home/pi/{timestamp}_image.jpg')  # Save the image with timestamp
    print(f"Image saved as /home/pi/{timestamp}_image.jpg")

def main():
    while True:
        if ser.in_waiting > 0:
            # Read data from Free Wili (assuming the sound level is sent as a value)
            data = ser.readline().decode('utf-8').strip()
            if data.isdigit():
                sound_level = int(data)  # Convert data to an integer
                print(f"Sound Level: {sound_level}")

                # Check if the sound level exceeds the threshold
                if sound_level > SOUND_THRESHOLD:
                    capture_image()

        time.sleep(0.1)

# Run the script
try:
    main()
except KeyboardInterrupt:
    print("Program interrupted. Cleaning up...")
finally:
    GPIO.cleanup()  # Clean up GPIO settings