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


class Client(ChatGui):
    def __init__(self, pseudo, address, port):
        

        self.address = address
        self.port = port
        self.pseudo = pseudo

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.connect((self.address, self.port))
        super().__init__()


        

    def send(self, message):

        if len(message.strip()) <= 0 :
            return
        elif executeCommand(message):
            self.msg.set("")
            return
        
        
        message = f"{self.pseudo} : " + message
        self.serverSocket.send(message.encode("utf-8"))
        
        self.msg.set("")

    def start(self):
        threading.Thread(target=self.recv).start()


    def recv(self):
        while True:
            try:
                recv = self.serverSocket.recv(1024)            
            except ConnectionResetError:
                print("ConnectionResetError")
                self.window.destroy()
                from Server import Server
                Server(self.pseudo, self.address, self.port)
                sys.exit()
                break
            
            if recv:
                print("recu chef")
                try:
                    obj = pickle.loads(recv)
                    # self.chat.delete(0, END)
                except:
                    self.recv()
                    return

                self.chat.delete(1.0, "end")

                while not pile_vide(obj):
                    self.chat.insert("1.0", depiler(obj).decode("utf-8") +"\n")
                    self.chat.see("1.0")

    


