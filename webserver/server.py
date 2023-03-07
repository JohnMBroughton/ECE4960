# echo-server.py

import socket
import struct
import sqlite3

#fucntons to update database
def updateDatabase(InorOut, ID, DBConn):
        if(InorOut == 0):
            remove_car(ID)
        elif(InorOut == 1):
            add_car(ID)
        else:
             print(InorOut + ": not a valid entrance or exit int")

def remove_car(ID):
        if(ID == 11111111):
            print("CUID not unpacked")
        else:
            print("sql call to remove car")
        #sql call to remove correspodign ID from the database


def add_car(ID):
        if(ID == 11111111):
            print("CUID not unpacked")
        else:
            print("sql call to add car")
        #sql call to add corresponding ID from Database

db_conn = sqlite3.connect("db.sq")
IoO = 2
CUID = 11111111

HOST = "169.254.185.103"  # This is the IP of the admin PC. This needs to be set statically
PORT = 5005  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created at %s:%d" % (HOST, PORT))
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(12)
            if not data:
                break
            else:
                print(struct.unpack('?ii',data))
                IoO = data[0]
                CUID = data[1]
                count = data[2]
                updateDatabase(IoO, CUID)

#conn.sendall(data)




