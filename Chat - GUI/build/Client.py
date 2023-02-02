#importation des nombreux modules

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

#Classe qui gère la connection client

class Client(ChatGui):
    def __init__(self, pseudo, address, port):
        
        #configuration de l'adresse et du port pour se connecter au serveur

        self.address = address
        self.port = port
        self.pseudo = pseudo



        self.index = 0;

        

        # Création d'un socket pour se connecter au serveur

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.connect((self.address, self.port))


        #Initialisation de la fenêtre (voir ChatGui.py)
        super().__init__()


        

    def send(self, message):
        # Vérifie si le message est vide
        if len(message.strip()) <= 0 :
            return

         # Vérifie si le message est une commande
        elif executeCommand(message):
            self.msg.set("")
            return
        
        # Sinon préfixe le pseudo à la message et l'envoie au serveur
        message = f"{self.pseudo} : " + message
        self.serverSocket.send(message.encode("utf-8"))
        
        self.msg.set("")

# Méthode pour démarrer un thread pour recevoir les messages

    def start(self):
        threading.Thread(target=self.recv).start()

# Méthode pour recevoir les messages
    def recv(self):
        while True:
            try:
                #essaie de recevoir un message
                recv = self.serverSocket.recv(1024)   #taille en byte du buffer          
            except ConnectionResetError:
                #si le serveur se déconnecte, on ferme la fenêtre et le client devient serveur
                print("ConnectionResetError")
                self.window.destroy()
                from Server import Server
                Server(self.pseudo, self.address, self.port)
                sys.exit()

            # Si un message est reçu
            
            if recv:
                # Désérialisation du message
                obj = pickle.loads(recv)             


                # Efface les messages précédents
                self.chat.delete(1.0, "end")

                self.afficheMessage(obj)

                



