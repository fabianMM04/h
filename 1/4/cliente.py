# Echo client program
import socket,pickle
from struct import *
HOST = '192.168.2.21'    # The remote host
PORT = 50006             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
data_arra=pickle.loads(data)
s.close()
print ('Received', repr(data_arra))