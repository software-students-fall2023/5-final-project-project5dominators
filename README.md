![CI, CD to Docker Hub, CD to Digital Ocean](https://github.com/software-students-fall2023/5-final-project-project5dominators/actions/workflows/webappCI-CD.yaml/badge.svg)


## Project Overview

This project involves the development of a unique chat application named "Snap&Chat". The core functionality of this application centers around the integration of real-time messaging with an innovative feature: users are required to send a selfie along with their text messages. This is achieved through a live camera feed, ensuring an interactive and authentic chatting experience. With thoughtful design shoices in UI/UX, as well as a modern and polished styling design, we aim to bring our users a relaxing and fun chatting experience. 

The full scope of this app is to function like most chatting apps where users can add friends, DM and create group chats. Due to time limitaion, we decided to implement the core functionality that makes this app stands out the most. Thus, we created a public chatroom, where users can join and drop messages along with their selfies in the chat. 

## Key Functionalities:

Live Camera Integration: Users can access their camera directly from the chat interface. This feature is essential for capturing selfies that are sent along with messages, promoting a more genuine and engaging communication experience.

Real-Time Messaging: The application supports real-time text messaging, allowing users to communicate instantly.

Image Processing Capabilities: (Accessed by ticking the "filter" check box)
Sketch Effect: Users have the option to convert their selfies into a sketch format before sending. This is done using image processing techniques such as edge detection and Gaussian blurring.
Cartoon Effect: Another creative feature is the ability to transform selfies into cartoon-style images. This is achieved through a combination of smoothing and edge detection techniques.

Message Deletion: Users can delete their messages from the chat, which then also removes them from the database.

Persistent Chat History: The chat history is stored in a MongoDB database, allowing users to view past conversations when they log in again.

Function to delele any message in the chatroom. (Prevents spamming, mostly by the Pytest bot)

Function to send message/take selfie both by clicking button and pressing Enter. 

Function to detect if client's camera is on and prevent user from sending messages if their camera is not on. 

Function to join/leave the chatroom. 

Function to pick any username and appear next to chat bubbles



## Links

[link to the image on DockerHub ](https://hub.docker.com/repository/docker/hyteve/snap-and-chat/general)


## Deployed WebApp Link

Link to server IP (Useless): http://165.227.106.8:5000/

Because accessing by IP is limited to HTTP, and most browsers only allow camera access on HTTPS websites, our app's core functionality of using camera is gone when using IP address. But it does fulfill the project requirement  :)

Link to domain (Inactive): https://snap-and-chat.com

We actually purchased this domain in order to use HTTPS. While setting up redirection routes, we realized that a website needs a SSL certificate to work in HTTPS. We have again purchased a certification for the website, but it is still pending and probably won't be approved in a few days  :(


As a result, please use the instructions in the following section to access our app. 

## How to confiure
```
- git clone https://github.com/software-students-fall2023/5-final-project-project5dominators
- cd 5-final-project-project5dominators
```
- Replace the following values with your MongoDB URI and secret key in app.py
```
MONGODB_URI = "your_mongodb_uri"
SECRET_KEY = "your_secret_key"
```


# TODO:

[instructions for how to configure and run all parts of your project for any developer on any platform - these instructions must work!]

[instructions for how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.]

## How to setup enviroment
### Ensure you have the required software installed:
- [Python](https://www.python.org/downloads/windows/)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [MongoDB](https://www.mongodb.com/docs/manual/installation/)
    *For MongoDB, If you use MongoDB Cluster, ignore it.*

## How to run
### Bash (Mac & Linux) / Command Prompt (Windows)

```
docker-compose up --build
visit the website on `http://localhost:5000` (Please make sure Carplay is turned off if you are using MacOS, as it will occupy port 5000)
```

## TESTING

Run tests using pytest:
```
pytest
```

## Importing Starter Data
- If your system relies on starter data, provide a script or instructions for importing it into the database: <br/>
`python import_data.py`


## Usage
### Live Camera Integration

    Access the camera directly from the chat interface.
    Tick the "filter" checkbox for additional image processing options.

### Image Processing Capabilities

    Sketch Effect: Convert selfies into a sketch format.
    Cartoon Effect: Transform selfies into cartoon-style images.

### Additional Functionalities

    Message Deletion: Delete messages from the chat.
    Persistent Chat History: Stored in the MongoDB database.
    Prevent Spamming: Functionality to delete any message in the chatroom.
    Send Message/Selfie: Click the button or press Enter.
    Camera Status Detection: Prevent sending messages if the camera is not on.
    Join/Leave Chatroom: Toggle your presence in the chat.
    Choose Username: Pick any username to appear next to chat bubbles.

## Team Members
- [Ethan Sha](https://github.com/EthanSha111)
- [Ashley Luo](https://github.com/luoashley)
- [Steve Hai](https://github.com/Hyteve)
