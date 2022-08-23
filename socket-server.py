import socket
from datetime import datetime
import numpy as np
import time
import argparse

# Add arg by user
parser = argparse.ArgumentParser()
parser.add_argument("--host", "-ho", default="0.0.0.0", type=str, required=False, help="your socket server hostname")
parser.add_argument("--port", "-po", default='6000', type=int, required=False, help="your socket server port")
args = parser.parse_args()

# Setup socket server parameter
HOST = args.host
PORT = args.port
FORMAT = "utf-8"

def systemTime():
    now = datetime.now()
    timeFormat = "%Y-%m-%d %H:%M:%S"
    formatTime = datetime.strftime(now, timeFormat)
    return formatTime

# setup socket server with parameter
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socketServer.bind((HOST, PORT))
except socket.error as e:
    print(f"[{systemTime()}][ERROR] {str(e)}")
    
        
# --------------------Service Loop Process--------------------------
print(f"[{systemTime()}][SERVER] Server is starting ...")
socketServer.listen()
print(f"[{systemTime()}][SERVER] Server Address: {HOST}:{PORT}")
print(f"[{systemTime()}][SERVER] Start to listen to client connection ...")
while True:
    # accept the connectio form outside
    print("Start to accept connection")
    conn, addr = socketServer.accept() # this cmd. will wait until receive next connection
    conn.send(bytes(f"[{systemTime()}][SERVER] Server Address: {HOST}:{PORT}", FORMAT))
    conn.send(bytes(f"[{systemTime()}][SERVER] numpy version: {np.__version__}", FORMAT))
    time.sleep(1)



