import os

from datetime import datetime
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)

#configuring socketio
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

#list to store chatroom names
chatlist = [] 

#list to store current users
usernames = []

#dictionary to store his/her message and time
messages = {}

#first page to display
@app.route("/")
def index():  
    return render_template("index.html")

#after entering name, take user to chat room
@app.route("/chatroom", methods=["POST"])
def chatroom():
   username = request.form.get("user_name")
   return render_template("channels.html", user_name=username)

#c
@socketio.on("submit channel")
def new_channel(data):
   selection = data["selection"]
   chatlist.append(selection)
   emit("announce channel", {"selection": data["selection"]}, chatlist=chatlist, broadcast=True)



   





