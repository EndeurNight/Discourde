#importation des modules
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


#Classe qui héberge la discussion et permet aussi de parler en toute sécurité à un client

class Server(ChatGui):
    def __init__(self, pseudo, address, port):

        #configuration de l'adresse et du port sur laquelle le serveur va écouter
        self.address = address
        self.port = port
        self.pseudo = pseudo
        
        #Création d'une pile pour stocker l'historique des messages
        self.history = creer_pile()

        #Création d'un socket pour écouter les clients
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind((self.address, self.port))
        self.listener.listen(1)
        

        #Initialisation de la fenêtre (voir ChatGui.py)
        super().__init__()



    def start(self):
        while True:
        #écoute la venu d'un client et le connecte
            print (f"Listening for clients on port {self.port}...")
            try:
                (client_socket, client_address) = self.listener.accept()
                self.client_sockets = client_socket
                self.client_sockets.send(pickle.dumps(self.history))
                threading.Thread(target=self.recv, args=(client_socket,)).start()
                return
                
            except socket.error:
                sys.exit("Connection error")

    def send(self, message):
        # Vérifie si le message est vide
        if len(message.strip()) <= 0 :
            return
        # Vérifie si le message est une commande
        elif executeCommand(message, self):
            self.msg.set("")
            return
        
        # Ajoute le pseudo au message
        message = f"{self.pseudo} : " + message
        
        # Ajoute le message à l'historique et l'envoie au client
        empiler(self.history, message.encode("utf-8"))
        self.refresh()
        pile = pickle.dumps(self.history)
        self.client_sockets.send(pile)
        
        self.msg.set("")

    def recv(self, socket):
        #Reçoit les messages du client et les ajoute à l'historique
        # Puis les renvoie au client pour qu'il puisse les afficher
        while True:            
            data = socket.recv(1024)
            if data:
                empiler(self.history, data)
                self.refresh()
                pile = pickle.dumps(self.history)
                self.client_sockets.send(pile)


    def refresh(self):
        # Rafraichit les messages affichés
        obj = self.history.copy()
        print(obj is self.history)
        self.chat.delete(1.0, "end")

        self.afficheMessage(obj)
                