from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask</p>
        <a href="/first">"Go first<a>
        <a href="/second>Go first<a>
        '''

@app.route("/First")
def first():
    return'''
    <p>First Page</p>
    <a href="/">GO Home</a>'''

@app.route("/Second")
def second():
    return'''
    <p>Second Page</p>
    <a href="/">GO Home</a>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0")
