from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/What")
def what():
    return {
        "What": "Is this?",
        "DoYouUnderstand": True,
        "HaveANumber": 5.5,
        "anotherProp": "Yup"
    }


@app.route("/github", methods=["POST"])
def githubRoot():
    print(request.get_json())
    return ('', 204)
