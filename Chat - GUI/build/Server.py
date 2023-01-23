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


class Server(ChatGui):
    def __init__(self, pseudo, address, port):
        super().__init__()

