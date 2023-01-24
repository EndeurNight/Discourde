import socket
import threading 
import sys
import pickle
from  Pile_Module import *

class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port

        self.client_sockets = []

        self.history = creer_pile()

        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind((self.address, self.port))
        self.listener.listen(1)
        threading.Thread(target=self.run).start()
        threading.Thread(target=self.send).start()


    def run(self):
        while True:
        #chercher client et creer client thread a chaque client
            print (f"Listening for clients on port {self.port}...")
            try:
                (client_socket, client_address) = self.listener.accept()
                self.client_sockets.append(client_socket)
                self.client_sockets[0].send(pickle.dumps(self.history))
                threading.Thread(target=self.recv, args=(client_socket,)).start()
                return
                
            except socket.error:
                sys.exit("erreur bc")

    def send(self):
        while True:
            msg = input("")

            msg = "Server : " + msg
            empiler(self.history, msg.encode("utf-8"))
            for socket in self.client_sockets:
                try:
                    
                    pile = pickle.dumps(self.history)
                    socket.send(pile)
                except socket.error:
                    print ("Impossible d'envoyer ton message")

    def recv(self, socket):
        while True:
            data = socket.recv(1024)
            if data:
                print(data.decode("utf-8"))
                empiler(self.history, data)
                pile = pickle.dumps(self.history)
                self.client_sockets[0].send(pile)
                # for socket in self.client_sockets:
                #     socket.send(data)
                # print(data.decode("utf-8"))
                
                
server = Server("localhost", 8080)

