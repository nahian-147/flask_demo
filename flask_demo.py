from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html',name='CDDA')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

app.run(port=8000, debug=True)