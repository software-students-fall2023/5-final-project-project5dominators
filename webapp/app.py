from flask import Flask, request, render_template, redirect, url_for,jsonify, session
from pymongo import MongoClient
from bson import ObjectId
from bson import json_util
from datetime import datetime
import base64
import json
import cv2


app = Flask(__name__)
# MongoDB connection setup
client = MongoClient("mongodb+srv://ys4323:Syysyysyy1@cluster0.ocmpb3f.mongodb.net/")
app.secret_key = 'ys4323'
db = client.SnapChat
users = db.User

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    user_exists = users.find_one({'username': username})

    if not user_exists:
        users.insert_one({'username': username})

    # Username is available, proceed to store in the database
    
    session['username'] = username  
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
    new_message = {
        'username': username,
        'message': message,
        'photo': imageData,
        'timestamp': timestamp
    }
    result = db.communication.insert_one(new_message)

   # Convert the ObjectId to a string
    new_message['_id'] = str(result.inserted_id)

    # Convert the timestamp to a string or a format that can be JSON serialized
    new_message['timestamp'] = str(timestamp)
    
    return jsonify(new_message)  # Return the new message


@app.route('/get_messages', methods=['GET'])
def get_messages():
    # Retrieve all messages and sort them in ascending order based on timestamp
    messages = list(db.communication.find().sort('timestamp', 1))

    # Convert MongoDB objects to JSON
    messages_json = json.loads(json_util.dumps(messages))

    return jsonify(messages_json)

@app.route('/delete_message/<message_id>', methods=['POST'])
def delete_message(message_id):
    try:
        # Convert message_id from string to ObjectId
        obj_id = ObjectId(message_id)
        db.communication.delete_one({'_id': obj_id})
        return jsonify({'status': 'success', 'message': 'Message deleted'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('home'))  # Redirect to the login page


if __name__ == '__main__':
    app.run(debug=True)