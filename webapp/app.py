from flask import Flask, request, render_template, redirect, url_for,jsonify, session
from pymongo import MongoClient
from bson import json_util
from datetime import datetime
import base64
import json


app = Flask(__name__)
# MongoDB connection setup
client = MongoClient("mongodb+srv://ys4323:Syysyysyy1@cluster0.ocmpb3f.mongodb.net/")
db = client.SnapChat
users = db.User

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    user_exists = users.find_one({'username': username})

    if user_exists:
        # Handle case where username is taken
        return render_template('login.html', error='Username taken, please choose another!')

    # Username is available, proceed to store in the database
    users.insert_one({'username': username})
    return redirect(url_for('main'))


@app.route('/main')
def main():
    return render_template('index.html')


@app.route('/post_message', methods=['POST'])
def send_message():
    username = session.get('username')
    message = request.form['message']
    imageData = request.form['image']
    timestamp = datetime.now()
    
    # Save the data to MongoDB
    db.communication.insert_one({
        'username': username,
        'message': message,
        'photo': imageData,
        'timestamp': timestamp
    })

    return jsonify({"status": "success"})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages = list(db.messages.find().sort('timestamp', -1))  # Fetch messages in descending order of timestamp
    return jsonify({'messages': messages})


if __name__ == '__main__':
    app.run(debug=True)