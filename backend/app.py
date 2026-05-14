from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app) 

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Task Manager API",
        "status": "running"
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tasks": [
            {"id": 1, "name": "Setup CI/CD Pipeline"},
            {"id": 2, "name": "Write Unit Tests"},
            {"id": 3, "name": "Deploy to Staging"},
            {"id": 4, "name": "Fix Memory Leak Bug"},
            {"id": 5, "name": "Update API Documentation"},
            {"id": 6, "name": "Refactor Auth Module"},
            {"id": 7, "name": "Add Rate Limiting"},
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
