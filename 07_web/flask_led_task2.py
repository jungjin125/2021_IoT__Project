from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_PIN=22
BLUE_PIN=27

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)


@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<op>/<color>")
def led_op(op, color):
    if (op == "on" and color=="RED"):
        GPIO.output(RED_PIN, GPIO.HIGH)
        return "RED LED ON"
    elif (op == "off" and color=="RED"):
        GPIO.output(RED_PIN, GPIO.LOW)
        return "RED LED OFF"
    elif (op == "on" and color=="BLUE"):
        GPIO.output(BLUE_PIN, GPIO.HIGH)
        return "BLUE LED ON"
    elif (op == "off" and color=="BLUE"):
        GPIO.output(BLUE_PIN, GPIO.LOW)
        return "BLUE LED OFF"
    else:
        return "ERROR"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
