from pathlib import Path
import socket
from tkinter import *
from Client import Client
from Server import Server
from ConfigGui import ConfigGui
from configparser import *

'''
Fenêtre Tkinter pour le menu principal de démarrage de Discourde 
'''


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainMenuGui:
    def __init__(self, pseudo="Guest", address="localhost", port=8080):
        self.address = address
        self.port = port
        self.pseudo = pseudo


        self.window = Tk()

        self.window.title("Chat")
        self.window.geometry("614x356")
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Discourde")

        config = ConfigParser()
        config.read("config.ini")

        self.mode = config["Serveur"]["mode"]

        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 356,
            width = 614,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

            #on place le fond
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
                307.0,
                178.0,
                image=image_image_1
        )


        
        canvas.create_rectangle(
            234.0,
            211.0,
            379.0,
            255.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            18.0,
            308.0,
            165.0,
            339.0,
            fill="#FFFFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.run(self.address, self.port),
            relief="flat"
        )
        button_1.place(
            x=234.0,
            y=211.0,
            width=145.0,
            height=43.5
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.config(),
            relief="flat"
        )
        button_2.place(
            x=18.0,
            y=308.0,
            width=147.0,
            height=31.0
        )

        #on place le logo
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
                313.0,
                115.0,
                image=image_image_2
            )


        self.window.resizable(False, False)
        self.window.mainloop()

    def run(self, address, port):
        try:
            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listener.bind((address,port))
            listener.close()
            self.window.destroy()
            print("")
            print("Chat configuration system not used.")
            print("Switching to server mode...")
            self.config.set("Serveur", "mode", "server")
            print("Server configuration:")
            print("Address: " + address)
            print("Port: " + str(port))
            print("")
            print("Starting server... (Press Ctrl+C to cancel)")
    
            Server(self.pseudo, self.address, self.port)
            
        except:
            print("")
            print("Chat configuration system used.")
            print("Switching to client mode...")
            self.config.set("Serveur", "mode", "client")
            print("Client configuration:")
            print("Address: " + address)
            print("Port: " + str(port))
            print("")
            print("Waiting for server... (Press Ctrl+C to cancel)")

            self.window.destroy()
            Client(self.pseudo, self.address, self.port)
            
        

    def config(self):
        self.window.destroy()
        ConfigGui()
        

    
