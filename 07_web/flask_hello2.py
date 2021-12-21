from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html",title="Hello, Flask!!")

@app.route("/First")
def first():
    return render_template("First.html")

@app.route("/Second")
def second():
    return render_template("Second.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
