#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    print('connect by ', addr)
    # while True:
    data = "<a href='http://google.com'>Google</a>"
    pack = ("HTTP/1.1 200 OK\nContent-type: text/html\nConnection: close\nContent-length: " + str(len(data)) + "\n\n" + data).encode('ascii')
    #data = data + ("Content-Length: " + (data.Length + 16)).encode('ascii')
        # if not data:
        #     break
    print(repr(pack))
    conn.send(pack)
    # conn.close()
s.close()

def addHeader(header, data):
    http_header = "HTTP/1.1"