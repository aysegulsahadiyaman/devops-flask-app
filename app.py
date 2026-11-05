from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Lab - Dockerized Flask App</h1>
    <p>My first containerized application is running!</p>
    <p>Environment: Ubuntu + Docker</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
