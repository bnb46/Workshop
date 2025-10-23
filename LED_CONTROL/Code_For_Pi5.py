from gpiozero import LED    # Import the GPIO library
from time import sleep      # Import the time library

led = LED(14)    # Tell python that your LED is on pin 14

while True: # While loop
    led.on()            # Turn the led ON
    print("LED is ON")  # Display confirmation message
    sleep(1)            # "sleep" (wait) for 1 second
    
    led.off()           # Turn the led OFF
    print("LED is OFF") # Display confirmation message
    sleep(1)            # "sleep" (wait) for 1 second
