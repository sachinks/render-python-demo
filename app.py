from flask import Flask, request
import os
app = Flask(__name__)


@app.route("/add")
def add_numbers():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        return f"Result: {a + b}"
    except:
        return "Please provide numbers like /add?a=2&b=3"

@app.route("/deduct")
def deduct_numbers():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        return f"Result: {a - b}"
    except:
        return "Please provide numbers like /deduct?a=2&b=3"


@app.route("/")
def home():
    return "Hello! This Python app is running on Render 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
