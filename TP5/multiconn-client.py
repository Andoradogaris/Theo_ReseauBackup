#multiconn-client.py

from pickle import TRUE
import sys
import socket
import selectors
import types
import keyboard
import traceback
import time
from tkinter import * 
from tkinter.messagebox import *


sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]
actionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)



def SendData():
    while TRUE:
        try:
            data = input("Sur quel case jouer ? : ")
            break
        except:
            print("numéro de case non valide")
    s.send(bytes(data, 'utf-8'))


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while TRUE:
            SendData()

            data = s.recv(1024).decode('utf-8')
            print(data)
            time.sleep(10)
except Exception as e :
    traceback.print_exc()
    print("Exit Client Connection")
    sys.exit(0)

print("toto")