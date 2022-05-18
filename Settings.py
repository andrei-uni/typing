from tkinter import *


class NewWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Settings")
        self.geometry("200x200")

    def setup(self):
        pass
