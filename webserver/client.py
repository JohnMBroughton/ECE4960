# echo-client.py

import socket
import struct

HOST = "169.254.185.103"  # The server's hostname or IP address
PORT = 5005  # The port used by the server

IoO = 1
CUID = 12345678

packet = struct.pack('?i', IoO, CUID)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet)
    data = s.recv(1024)

print(f"Received {data!r}")
