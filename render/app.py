from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chedo')
def hello_chedo():
    return 'Welcome to chedo Tech'
