import socket

address = ""
port = 8080

try:
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((address, port))
    listener.close()
    from Server import *
except:
    print("deja connecte")
    from Client import *
    