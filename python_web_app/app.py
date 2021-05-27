from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from postgress_connection import postgress_connection

import socket
import sys
import time


app = Flask(__name__)

@app.route("/")
def index():
    ip_address = request.remote_addr
    path = request.path
    hostname_container = socket.gethostname()
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")

    writeToFile(ip_address, path, hostname_container, time)

   
    conn = postgress_connection()
    conn.insert(ip_address, path, hostname_container, time)
    conn.selectAll()
    conn.close()

    return render_template("index.html", **locals())

@app.route("/hi")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"

def writeToFile(ip_address, path, hostname_container, time):
    f = open("/tmp/requests.txt", "a")
    f.write("IP Adress: " + ip_address + "\n")
    f.write("PATH: " + path  + "\n")
    f.write("Hostname: " + hostname_container + "\n")
    f.write("Time: " + time + "\n")
    f.write("--------------------------------------------------\n")
    f.close()

def writeToDatabase(ip_address, path, hostname_container, time):
    # Code here
    conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

