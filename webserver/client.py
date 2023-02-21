# echo-client.py

import socket
import struct

HOST = "169.254.185.103"  # The server's hostname or IP address
PORT = 5005  # The port used by the server

ID = 1
count = 9

packet = struct.pack('hh', ID, count)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet)
    data = s.recv(1024)

print(f"Received {data!r}")
