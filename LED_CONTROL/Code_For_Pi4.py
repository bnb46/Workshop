import RPi.GPIO as GPIO    # Import the GPIO interface library
import time                # Import the time library

GPIO.setmode(GPIO.BCM)     # Tells python what pin naming convention we are using
GPIO.setwarnings(False)    # Ignore warnings (we live life on the edge)
GPIO.setup(14,GPIO.OUT)    # Set pin 14 to output mode

while True: # While loop
    GPIO.output(14,GPIO.HIGH)    # Turn your led ON
    print("LED is ON")           # Display confirmation message
    time.sleep(1)                # "sleep" (wait) for 1 second

    GPIO.output(14,GPIO.LOW)     # Turn your led OFF
    print("LED is OFF")          # Display confirmation message

    time.sleep(1)                # "sleep" (wait) for 1 second
