from pathlib import Path
from tkinter import *
import socket
from configparser import *

'''
Fenêtre Tkinter pour les paramètres du chat (IP, port, pseudo)
'''

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ConfigGui:
    def __init__(self):        

        self.window = Tk()

        self.window.geometry("614x356")
        self.window.configure(bg = "#FFFFFF")

        self.address = StringVar()
        self.port = StringVar()
        self.pseudo = StringVar()
        self.window.title("Control panel")

        #on initialise le fichier de config
        self.config = ConfigParser()
        self.config.read('config.ini')

        self.address.set(self.config['Utilisateur']['pseudo'])
        self.pseudo.set(self.config['Utilisateur']['pseudo'])
        self.pseudo.set(self.pseudo.get().replace(" ", ""))
        self.address.set(self.config['Serveur']['ip'])
        self.port.set(self.config['Serveur']['port'])

        print("\r")
        print("Opening config window...")
        print("Actual config:")
        if self.pseudo.get() == "":
            print("Pseudo is empty, using default value (Guest)")
            self.pseudo.set("Guest")
        else:
            print("Pseudo: " + self.pseudo.get())
        
        if self.address.get() == "":
            print("Address is empty, using default value (localhost)")
            self.address.set("localhost")
        else:
            print("Address: " + self.address.get())
        
        if self.port.get() == "":
            print("Port is empty, using default value (8080)")
            self.port.set("8080")
        else :
            print("Port: " + self.port.get())
        
        with open('config.ini', 'w') as configfile:
            self.config['Serveur']['ip'] = self.address.get()
            self.config['Serveur']['port'] = self.port.get()
            self.config['Utilisateur']['pseudo'] = self.pseudo.get()
            self.config.write(configfile)



        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 356,
            width = 614,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            464.0,
            303.0,
            594.0,
            335.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            404.0,
            181.0,
            581.0,
            224.0,
            fill="#FFFFFF",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            197.5,
            273.0,
            image=self.entry_image_1
        )


        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            304.0,
            162.0,
            image=self.entry_image_2
        )
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            118.5,
            162.0,
            image=self.entry_image_3
        )
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            191.0,
            272.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            299.0,
            164.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            119.0,
            163.0,
            image=self.image_image_3
        )
        

        
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.address
        )
        self.entry_3.place(
            x=36.0,
            y=150.0,
            width=165.0,
            height=22.0
        )

        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.port
        )
        self.entry_2.place(
            x=257.0,
            y=150.0,
            width=94.0,
            height=22.0
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.pseudo
            )
        
        self.entry_1.place(
            x=44.0,
            y=262.0,
            width=307.0,
            height=20.0
        )

        self.edit_button_image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.edit_button = Button(
            image=self.edit_button_image,
            borderwidth=0,
            highlightthickness=0,
                       command=lambda: print("Currently not working. We are working on it."),            #command=lambda: print(self.address.get() + self.port.get() +self.pseudo.get()),
            relief="flat"
        )
        self.edit_button.place(
            x=404.0,
            y=181.0,
            width=177.0,
            height=43.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.Save(),
            relief="flat"
        )
        self.button_2.place(
            x=470.0,
            y=310.0,
            width=130.0,
            height=32.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            278.0,
            57.0,
            image=self.image_image_4
        )
        self.window.resizable(False, False)
        self.window.mainloop()


    def Save(self):
        address = self.address.get()
        self.config.set("Serveur", "ip", str(address))
        assert self.port.get().isdigit(), "Port must be a number"
        port = int(self.port.get())
        self.config.set("Serveur", "port", str(port))
        pseudo = self.pseudo.get()
        assert pseudo != "", "Pseudo must not be empty"
        assert pseudo.isalnum(), "Pseudo must be alphanumeric"
        self.config.set("Utilisateur", "pseudo", str(pseudo))
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        print("Config saved")
        self.window.destroy()
        from MainMenuGui import MainMenuGui
        MainMenuGui(pseudo, address, port)
        

        


