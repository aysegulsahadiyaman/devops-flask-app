import os
from flask import Flask

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return f"""
    <h1>DevOps Lab - Dockerized Flask App</h1>
    <p>My first containerized application is running!</p>
    <p>Environment: {APP_ENV}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
