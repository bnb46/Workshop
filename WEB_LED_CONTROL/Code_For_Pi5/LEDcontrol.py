from gpiozero import LED
from time import sleep
from flask import Flask, render_template, request
import subprocess

# Setup Flask app
app = Flask(__name__)
# Detailed explanation - this creates an instance of the Flask class and assigns it to the app
# variable to use as an object. __name__ is a special Python variable that indicates the current script's name. 
# Flask uses this to determine the root path for your project.

# Set up which pin you want to use for your LED
led = LED(14)

# Route for the main webpage
@app.route('/')
def interface():
    return render_template('interface.html')

# Route to turn the LED ON or OFF
@app.route('/led', methods=['POST']) # Posting happens when a user interacts with a webpage.
def led():
    state = request.form['state']
    if state == 'ON':
        led.on()  # Turn LED on
        print("LED is ON")
    else:
        led.off() # Turn LED off
        print("LED is OFF")
    return '', 204  # Return no content


# Function to terminate Flask server process
def terminate_flask():
    # Find the PID of the process using port 5000 and kill it
    subprocess.run("sudo lsof -t -i:5000 | xargs sudo kill -9", shell=True)
    
# Run the Flask app
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("Keyboard Interrupt received. Cleaning up...")
        terminate_flask()  # Kill the process holding the port 5000


