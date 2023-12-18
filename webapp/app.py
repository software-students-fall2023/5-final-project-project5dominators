from flask import Flask, request, render_template, redirect, url_for,jsonify, session
from pymongo import MongoClient
from bson import ObjectId
from bson import json_util
from datetime import datetime
import numpy as np
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

    # Manually convert each message to a JSON-friendly format
    messages_json = []
    for message in messages:
        message['_id'] = str(message['_id'])  # Convert ObjectId to string
        message['timestamp'] = str(message['timestamp'])  # Convert timestamp to string if necessary
        messages_json.append(message)

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

@app.route('/convert_to_sketch', methods=['POST'])
def convert_to_sketch():
    username = session.get('username')
    message = request.form['message']
    timestamp = datetime.now()
    # Extract the image from the request
    image_data = request.form['image']
    # Decode the image from base64
    encoded_data = image_data.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Apply Canny Edge Detector
    edges = cv2.Canny(blurred_image, 100, 200)

    # Encode the result
    _, buffer = cv2.imencode('.jpg', edges)
    sketch_base64 = base64.b64encode(buffer).decode('utf-8')
    new_message = {
        'username': username,
        'message': message,
        'photo': 'data:image/jpeg;base64,' + sketch_base64,
        'timestamp': timestamp
        }
    result = db.communication.insert_one(new_message)

    # Convert the ObjectId to a string
    new_message['_id'] = str(result.inserted_id)

    # Convert the timestamp to a string or a format that can be JSON serialized
    new_message['timestamp'] = str(timestamp)
    return jsonify(new_message)

@app.route('/convert_to_cartoon', methods=['POST'])
def convert_to_cartoon():
    username = session.get('username')
    message = request.form['message']
    timestamp = datetime.now()
    
    # Extract the image from the request
    image_data = request.form['image']
    
    # Decode the image from base64
    encoded_data = image_data.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur
    gray_blur = cv2.medianBlur(gray, 5)
    
    # Retrieve edges using adaptive threshold
    edges = cv2.adaptiveThreshold(gray_blur, 255, 
                                    cv2.ADAPTIVE_THRESH_MEAN_C, 
                                    cv2.THRESH_BINARY, 9, 9)
    
    # Apply bilateral filter to get cartoonish look
    color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # Combine edges and color
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Encode the result
    _, buffer = cv2.imencode('.jpg', cartoon)
    cartoon_base64 = base64.b64encode(buffer).decode('utf-8')

    new_message = {
        'username': username,
        'message': message,
        'photo': 'data:image/jpeg;base64,' + cartoon_base64,
        'timestamp': timestamp
    }
    result = db.communication.insert_one(new_message)

    # Convert the ObjectId to a string
    new_message['_id'] = str(result.inserted_id)

    # Convert the timestamp to a string for JSON serialization
    new_message['timestamp'] = str(timestamp)
    return jsonify(new_message)


@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('home'))  # Redirect to the login page


if __name__ == '__main__':
    app.run(debug=True)