import socket, os, sys
import threading
import pickle
from ChatGui import *
from pathlib import Path
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import colorchooser
from Pile_Module import *
from commands import *

class Server(ChatGui):
    def __init__(self, pseudo, address, port):
        self.address = address
        self.port = port
        self.pseudo = pseudo

        self.history = creer_pile()

        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind((self.address, self.port))
        self.listener.listen(1)
        
        super().__init__()



    def start(self):
        while True:
        #chercher client et creer client thread a chaque client
            print (f"Listening for clients on port {self.port}...")
            try:
                (client_socket, client_address) = self.listener.accept()
                self.client_sockets = client_socket
                self.client_sockets.send(pickle.dumps(self.history))
                threading.Thread(target=self.recv, args=(client_socket,)).start()
                return
                
            except socket.error:
                sys.exit("erreur bc")

    def send(self, message):

        if len(message.strip()) <= 0 :
            return
        elif executeCommand(message):
            self.msg.set("")
            return
        
        
        message = f"{self.pseudo} : " + message

        empiler(self.history, message.encode("utf-8"))
        self.refresh()
        pile = pickle.dumps(self.history)
        self.client_sockets.send(pile)
        
        self.msg.set("")

    def recv(self, socket):
        while True:
            data = socket.recv(1024)
            if data:
                empiler(self.history, data)
                self.refresh()
                pile = pickle.dumps(self.history)
                self.client_sockets.send(pile)


    def refresh(self):
        obj = self.history.copy()
        print(obj is self.history)
        self.chat.delete(1.0, "end")

        while not pile_vide(obj):
            self.chat.insert("1.0", depiler(obj).decode("utf-8") +"\n")
            self.chat.see("1.0")
                