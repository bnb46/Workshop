import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

while True:
    GPIO.output(14,GPIO.HIGH)
    print("LED is ON")
    time.sleep(1)

    GPIO.output(14,GPIO.LOW)
    print("LED is OFF")
    time.sleep(1)