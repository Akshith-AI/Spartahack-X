import serial
import time

ser = serial.Serial('/dev/serial10', 115200, timeout=1)

if ser.is_open:
    print(b"Uart connection found")

    ser.write(b"Hello WILi world")

    while True:
        if ser.in_waiting > 0:  # Fix: 'i_writing' -> 'in_waiting'
            data = ser.readline().decode('utf-8').strip()  # Fix: 'script()' -> 'strip()'
            print(f"Received: {data}")

        time.sleep(1)  # Fix: 'time sleep(1)' -> 'time.sleep(1)'

    ser.close()