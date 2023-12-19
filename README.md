![CI, CD to Docker Hub, CD to Digital Ocean](https://github.com/software-students-fall2023/5-final-project-project5dominators/actions/workflows/webappCI-CD.yaml/badge.svg)


## Project Overview

This project involves the development of a unique chat application named "Snap&Chat". The core functionality of this application centers around the integration of real-time messaging with an innovative feature: users are required to send a selfie along with their text messages. This is achieved through a live camera feed, ensuring an interactive and authentic chatting experience. 

The full scope of this app is to function like most chatting apps where users can add friends, DM and create group chats. Due to time limitaion, we decided to implement the core functionality where this app stands out the most. Thus, we created a public chatroom, where user can join and drop messages along with their selfies in the chat. 

# Key Functionalities:

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

Because accessing by IP is limited to HTTP, and most browser would not allow camera access on HTTP websites, which disables the core functionality for our website. But it does satisfies the project requirement  :)

Link to domain (Inactive): https://snap-and-chat.com

We actually purchased this domain in order to use HTTPS. While setting up redirection routes, we realized that it needs a SSL certificate to work in HTTPS. We have again purchased a certification for the website, but it is still pending and probably won't be approved in a few days  :(

As a result, please use the instructions in the following sections to access our app. 

## Configuration Instructions
- download dockerhub
- clone the repository
- cd to the main directory and run  `docker-compose up --build`
- visit the website on `http://localhost:5000` (Please make sure Carplay is turned off if you are using MacOS, as it will occupy port 5000)


## Team Members
- [Ethan Sha](https://github.com/EthanSha111)
- [Ashley Luo](https://github.com/luoashley)
- [Steve Hai](https://github.com/Hyteve)
