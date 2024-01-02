import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "My name is Vinayak Dubey and USN 1BM20IS182"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
