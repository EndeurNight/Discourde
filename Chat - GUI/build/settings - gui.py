'''
Fenêtre Tkinter pour les paramètres de thème
'''


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("614x356")
window.configure(bg = "#FFFFFF")
window.title("Discourde theme settings")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 356,
    width = 614,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    527.0,
    115.0,
    559.0,
    148.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    527.0,
    160.0,
    559.0,
    193.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    527.0,
    205.0,
    559.0,
    238.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    527.0,
    250.0,
    559.0,
    283.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    470.0,
    310.0,
    600.0,
    342.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=470.0,
    y=310.0,
    width=130.0,
    height=32.0
)

canvas.create_text(
    392.088623046875,
    120.67568969726562,
    anchor="nw",
    text="#H5HPHY",
    fill="#1C1B1F",
    font=("RobotoRoman Bold", 16 * -1)
)

canvas.create_rectangle(
    351.0,
    122.0,
    369.71319580078125,
    141.8333282470703,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    392.088623046875,
    165.67568969726562,
    anchor="nw",
    text="#H5HPHY",
    fill="#1C1B1F",
    font=("RobotoRoman Bold", 16 * -1)
)

canvas.create_rectangle(
    352.0,
    167.0,
    370.71319580078125,
    186.83334350585938,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    392.088623046875,
    210.6756591796875,
    anchor="nw",
    text="#H5HPHY",
    fill="#1C1B1F",
    font=("RobotoRoman Bold", 16 * -1)
)

canvas.create_rectangle(
    351.0,
    212.0,
    369.71319580078125,
    231.83334350585938,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    392.088623046875,
    255.6756591796875,
    anchor="nw",
    text="#H5HPHY",
    fill="#1C1B1F",
    font=("RobotoRoman Bold", 16 * -1)
)

canvas.create_rectangle(
    351.0,
    257.0,
    369.71319580078125,
    276.8333435058594,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    164.0,
    57.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    173.0,
    139.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    142.0,
    184.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    167.0,
    234.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    151.0,
    274.0,
    image=image_image_5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=527.0,
    y=115.0,
    width=32.0,
    height=33.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=527.0,
    y=160.0,
    width=32.0,
    height=33.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=527.0,
    y=205.0,
    width=32.0,
    height=33.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=527.0,
    y=250.0,
    width=32.0,
    height=33.0
)
window.resizable(False, False)
window.mainloop()
