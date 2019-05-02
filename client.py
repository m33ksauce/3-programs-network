#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # msg = input("What's your message?")
    s.sendall(b'test')
    data = s.recv(1024)
print('Received ', repr(data))
