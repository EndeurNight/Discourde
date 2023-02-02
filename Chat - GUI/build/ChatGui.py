from pathlib import Path
from tkinter.ttk import Combobox
from tkinter import *
from triFusion import *
from configparser import *

'''
Fenetres Tkinter principale avec la fenêtre du chat
'''

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ChatGui:
    def __init__(self) :
        self.window = Tk()

        self.window.geometry("1060x650")
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Discourde")
        #self.window.iconbitmap('build/assets\other\logo.ico')

        self.msg = StringVar()
        self.config = ConfigParser()
        self.config.read('config.ini')


        if self.pseudo == "":
            self.pseudo = "Anonyme             "
        if len(self.pseudo) < 20:
            self.pseudo = self.pseudo + " " * (20 - len(self.pseudo))


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 650,
            width = 1060,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            333.0,
            624.0,
            anchor="nw",
            text="Connecté en tant que  : " + self.pseudo + " | Discourde (" + self.mode + ") build 2.4",
            fill="#000000",
            font=("RobotoRoman Regular", 11 * -1)
        )

        self.chat = Text(
            self.window,
            bd = 0,
            bg = "#FFFFFF",
            highlightthickness = 0
        )

       

        self.chat.place(
            x = 20,
            y = 20,
            width = 1019,
            height = 450
        )

        self.chat.bind("<Key>", lambda e: "break")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            530.0,
            581.0,
            image=self.image_image_1
        )
        '''
        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            530.0,
            271.0,
            image=self.image_image_2
        )
        '''

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            530.0,
            575.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#008000",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.msg
        )
        self.entry_1.place(
            x=102.0,
            y=553.0,
            width=856.0,
            height=42.0
        )

        

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=54.0,
            y=559.0,
            width=31.0,
            height=32.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))

        


        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.send(self.msg.get()),
            relief="flat"
        )

        self.button_2.place(
            x=976.0,
            y=559.0,
            width=32.0,
            height=32.0
        )


        self.fonts_list = Combobox(
            values = getPolice(),
            state = "readonly",
        )

        self.fonts_list.bind("<<ComboboxSelected>>", lambda e: self.chat.config(font=(self.fonts_list.get(), 12)))
        self.fonts_list.pack()

        self.fonts_list.current(0)

        
        self.entry_1.bind("<Return>", lambda e :self.send(self.msg.get()))

        self.chat.config(font=(self.fonts_list.get(), 12))
        self.window.resizable(False, False)
        self.start()
        self.window.mainloop()


    

    def send(self, msg):
        print("send")


    def start(self):
        print("starting")

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

#test de la fenêtre
#test = ChatGui()
