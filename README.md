# Webhook in Python with Flask

This project implements a basic server using Python and Flask to receive webhook requests and process them. The server responds with a confirmation message, demonstrating how to create a simple Webhook architecture.

## Clone the repository
Use the command in your terminal:

```bash
git clone https://github.com/Karen020701/App-Webhook.git
```

## Install dependencies
Install Flask and the Flask-CORS extension, which enables cross-origin requests (CORS):
```bash
pip install Flask flask-cors
```

## Run the server

Once the dependencies are installed, you can start the server by running the following command:
```bash
python app.py
```
In the console section, you will see the server running: Running on http://127.0.0.1:5000

##Flask Webhook

The server listens for requests on the /AppWebhook path using the GET method.
That is, the request would be: http://127.0.0.1:5000/webhook

As a result, the server displays:
"message": "Hello World with Webhook in Python"

![image](https://github.com/user-attachments/assets/56d332f9-53fb-4072-94a2-b104a37ff4dd)
