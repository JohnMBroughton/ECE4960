# echo-server.py

import socket
import struct
import sqlite3

#fucntons to update database
def updateDatabase(InorOut, ID, databaseConnection):
        if(InorOut == 0):
            remove_car(ID, databaseConnection)
        elif(InorOut == 1):
            add_car(ID, databaseConnection)
        else:
             print(InorOut + ": not a valid entrance or exit value")

def remove_car(ID, databaseConnection):
        if(ID == 11111111):
            print("CUID not unpacked")
        else:
            print("sql call to remove car")
            databaseConnection.execute("DELETE FROM table_name WHERE CUID =(?)", ID)
            

def add_car(ID, databaseConnection):
        if(ID == 11111111):
            print("CUID not unpacked")
        else:
            print("sql call to add car")
            databaseConnection.execute("INSERT into table_name (column1, column2) V")
        

DB_conn = sqlite3.connect('databaseName.db') #Connect to the database


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
                updateDatabase(IoO, CUID, DB_conn)

#conn.sendall(data)




