import socket, os, sys
import threading
import pickle

from Pile_Module import *

from pathlib import Path

from triFusion import *
from commands import *

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *

from tkinter import colorchooser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\cludw\Documents\GitHub\NSIProjetX\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

################################################################################################



################################################################################################


class GUI:
    def __init__(self, address, port) :  

        self.address = address
        self.port = port
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.address, self.port))
        # threading.Thread(target=self.run).start()
        threading.Thread(target=self.recv).start()     

        window = Tk()

        window.geometry("1060x660")
        window.configure(bg = "#FFFFFF")

        window.wm_attributes('-transparentcolor', '#FFFFF1')


        self.chatHistory = StringVar()
        self.chatHistory.set("test")
        self.msg = StringVar()

        self.color = "#ff4246"


        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 660,
            width = 1060,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)


        self.chat = Text(
            window,
            bd = 0,
            bg = self.color,
            highlightthickness = 0
        )

       

        self.chat.place(
            x = 20,
            y = 20,
            width = 1019,
            height = 450
        )

        self.chat.bind("<Key>", lambda e: "break")

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            533.0,
            330.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            530.0,
            330.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            447.0,
            582.0,
            image=image_image_3
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.send2(self.msg.get()),
            relief="flat"
        )
        button_1.place(
            x=875.0,
            y=550.0,
            width=134.0,
            height=65.0
            
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png")
            )
        entry_bg_1 = canvas.create_image(
            444.5,
            583.0,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.msg
        )
        self.entry_1.place(
            x=60.0,
            y=559.0,
            width=769.0,
            height=46.0
        )

        self.entry_1.bind("<Return>", lambda e :self.send2(self.msg.get()))

        self.fonts_list = Combobox(
            values = getPolice(),
            state = "readonly",
        )

        self.fonts_list.bind("<<ComboboxSelected>>", lambda e: self.chat.config(font=(self.fonts_list.get(), 12)))
        self.fonts_list.pack()

        self.fonts_list.current(0)

        self.colorPicker = Button(
            command= lambda:self.chooseColor()
        )

        self.colorPicker.pack()


        self.chat.config(font=(self.fonts_list.get(), 12))
        window.resizable(False, False)
        window.mainloop()

    def send2(self, message):

        if len(message.strip()) <= 0 :
            return
        elif executeCommand(message):
            self.msg.set("")
            return
        
        
        message = "Client : " + message
        self.client.send(message.encode("utf-8"))
        
        self.msg.set("")

    def start(self):
        threading.Thread(target=self.recv).start()

       

    def recv(self):
        while True:
            try:
                recv = self.client.recv(1024)            
            except ConnectionResetError:
                print("ConnectionResetError")
                self.window.destroy()
                os.system("python Server.py")
                sys.exit()
                break
            
            if recv:
                try:
                    obj = pickle.loads(recv)
                    self.chatHistory.set("")
                    # self.chat.delete(0, END)
                except:
                    self.recv()
                    return

                self.chat.delete(1.0, "end")
                #with Text
                while not pile_vide(obj):
                    self.chat.insert("1.0", depiler(obj).decode("utf-8") +"\n")
                    self.chat.see("1.0")

    def chooseColor(self):
        self.color = colorchooser.askcolor(title ="Choose color")[1]
        self.chat.config(bg=self.color)


def getPolice():
    from matplotlib import font_manager
    fonts = font_manager.findSystemFonts()
    fonts_name = []
    for font in fonts:
        font_prop = font_manager.FontProperties(fname=font)
        fonts_name.append(font_prop.get_name())
    fonts_name = trifusion(fonts_name)
    fonts_name = remove_duplicates(fonts_name)
    return fonts_name


gui = GUI("localhost", 8080)
gui.start()