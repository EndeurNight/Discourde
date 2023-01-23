import socket, os, sys
import threading
import pickle

from ChatGui import *

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import colorchooser
from Pile_Module import *


class Client(ChatGui):
    def __init__(self, pseudo, address, port):
        super().__init__()

        self.address = address
        self.port = port
        self.pseudo = pseudo


        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.address, self.port))
        # threading.Thread(target=self.run).start()
        threading.Thread(target=self.recv).start()   



        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.send(self.msg.get()),
            relief="flat"
        )


        
        self.entry_1.bind("<Return>", lambda e :self.send(self.msg.get()))

    def send(self, message):

        if len(message.strip()) <= 0 :
            return
        # elif executeCommand(message):
        #     self.msg.set("")
        #     return
        
        
        message = "Client : " + message
        self.client.send(message.encode("utf-8"))
        
        self.msg.set("")

    def start(self):
        threading.Thread(target=self.recv).start()

    


