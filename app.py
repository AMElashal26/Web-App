#app.py

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/todoDatabase"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = mongo.db.tasks
    task = request.json['task']
    task_category = "General"  # Placeholder for category, until ML model is integrated
    task_id = tasks.insert_one({'task': task, 'category': task_category}).inserted_id
    new_task = tasks.find_one({'_id': task_id})
    return jsonify(task=new_task['task'], category=new_task['category']), 201
