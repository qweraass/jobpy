import socket
import time
import datetime



IP = "127.0.0.1"
PORT = 1101


try:
    
    print("jobpy => hello.py => GitHub ")
    print(f"{IP}:{PORT}")
    so = socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(10)
    so.connect(IP, PORT)

finally:
    exit(0)