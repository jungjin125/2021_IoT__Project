from flask import Flask
import RPi.GPIO as GPIO

LED_PIN=22

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask</p>
        <a href="/led/on">led on<a>
        <a href="/led/off">led off<a>
        '''

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return'''
        <p>LED ON</p>
        <a href="/">GO Home</a>'''
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return'''
        <p>LED OFF</p>
        <a href="/">GO Home</a>'''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
