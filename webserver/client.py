#!/usr/bin/env python3
# client.py
# ECE 4960 - Clemson University - Team 14
#
# This program connects via socket to the server and will read RFID tag data
# from the reader, pack the data, and send it to the server. It is based on
# the following file - https://github.com/realpython/materials/blob/master/python-sockets-tutorial/echo-client.py

import socket
import struct
import rfid

HOST = "169.254.185.103"  # The server's hostname or IP address
PORT = 5005  # The port used by the server

IoO = 1
CUID = 12345678

count = 0

#packet = struct.pack('?i', IoO, CUID)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        #while True:
        input("Press enter to continue:") #Replaces interrupt
        CUID = rfid.GetCUID()
        packet = struct.pack('?8s', IoO, CUID)
        s.sendall(packet)


