# Echo server program
import socket, pickle
from struct import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50006             # Arbitrary non-privileged port
cliente=['cliente1','cliente2']
data_string=pickle.dumps(cliente)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    try:

        conn.sendall(data_string)
    finally:
        conn.close()

