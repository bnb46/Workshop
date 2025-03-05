from gpiozero import LED
from flask import Flask, render_template, request
import time
import subprocess

# Setup the LED using gpiozero
led = LED(14)

# Setup Flask app
app = Flask(__name__)

# Route for the main webpage
@app.route('/')
def interface():
    return render_template('interface.html')

# Route to turn the LED ON or OFF
@app.route('/led', methods=['POST'])
def led_control():
    state = request.form['state']
    if state == 'ON':
        led.on()  # Turn LED on
        print("LED is ON")
    else:
        led.off()  # Turn LED off
        print("LED is OFF")
    return '', 204  # Return no content

# Function to terminate Flask server process
def terminate_flask():
    subprocess.run("sudo lsof -t -i:5000 | xargs sudo kill -9", shell=True)
    
# Run the Flask app
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("Keyboard Interrupt received. Cleaning up...")
        terminate_flask()  # Kill the process holding the port 5000
        led.close()  # Properly release LED resource
        print("Cleanup done and port 5000 is released.")
