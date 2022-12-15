import os
from flask import Flask

app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 3200

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )