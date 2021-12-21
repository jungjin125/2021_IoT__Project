from flask import Flask
import RPi.GPIO as GPIO

RED_PIN=22
BLUE_PIN=27

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask</p>
        <a href="/led/RED/on">RED led on<a>
        <a href="/led/RED/off">RED led off<a>
        <a href="/led/BLUE/on">BLUE led on<a>
        <a href="/led/BLUE/off">BLUE led off<a>
        '''

@app.route("/led/<color>/<op>")
def led_op(color,op):
    if color == "RED":
        if op == "on":
            GPIO.output(RED_PIN, GPIO.HIGH)
            return'''
            <p>RED LED ON</p>
            <a href="/">GO Home</a>'''
        elif op == "off":
            GPIO.output(RED_PIN, GPIO.LOW)
            return'''
            <p>RED LED OFF</p>
            <a href="/">GO Home</a>'''

            
    elif color == "BLUE":
        if op == "on":
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            return'''
            <p>BLUE LED ON</p>
            <a href="/">GO Home</a>'''
        elif op == "off":
            GPIO.output(BLUE_PIN, GPIO.LOW)
            return'''
            <p>BLUE LED OFF</p>
            <a href="/">GO Home</a>'''
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
