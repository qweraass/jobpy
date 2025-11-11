import socket
import time
import datetime



IP = "127.0.0.1"
PORT = 1101


try:
    
    print(f"{IP}:{PORT}")
    so = socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(10)
    so.connect(IP, PORT)

    so.close()


if __main__ = "__main__":
    printf("main")