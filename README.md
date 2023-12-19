
## Project Overview

This project involves the development of a unique chat application named "Snap&Chat". The core functionality of this application centers around the integration of real-time messaging with an innovative feature: users are required to send a selfie along with their text messages. This is achieved through a live camera feed, ensuring an interactive and authentic chatting experience.

# Key Functionalities:

Live Camera Integration: Users can access their camera directly from the chat interface. This feature is essential for capturing selfies that are sent along with messages, promoting a more genuine and engaging communication experience.

Real-Time Messaging: The application supports real-time text messaging, allowing users to communicate instantly.

Image Processing Capabilities:

Sketch Effect: Users have the option to convert their selfies into a sketch format before sending. This is done using image processing techniques such as edge detection and Gaussian blurring.
Cartoon Effect: Another creative feature is the ability to transform selfies into cartoon-style images. This is achieved through a combination of smoothing and edge detection techniques.
Message Deletion: Users can delete their messages from the chat, which then also removes them from the database.

Persistent Chat History: The chat history is stored in a MongoDB database, allowing users to view past conversations when they log in again.



![CI](https://github.com/software-students-fall2023/5-final-project-project5dominators/actions/workflows/webappCI-CD.yaml/badge.svg)


## Links

[link to the image on DockerHub ](https://hub.docker.com/repository/docker/hyteve/snap-and-chat/general)

[Link to Server IP]() (Impractical. Because accessing by IP is limited to HTTP, but most browser would not allow camera access in HTTP websites, which disables the core functionality for our website. )

Link to domain: 

## Configuration Instructions
- download dockerhub
- clone the repository
- cd to the main directory and run  `docker-compose up --build`
- visit the website on `http://localhost:5001`

## Deployed WebApp Link


## Team Members
- [Ethan Sha](https://github.com/EthanSha111)
- [Ashley Luo](https://github.com/luoashley)
- [Steve Hai](https://github.com/Hyteve)
