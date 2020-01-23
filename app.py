from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/What")
def what():
    return {
        "What": "Is this?",
        "DoYouUnderstand": True,
        "HaveANumber": 5.5
    }