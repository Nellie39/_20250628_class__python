from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloe_world():
    return "<p>Hello, World!</p>"