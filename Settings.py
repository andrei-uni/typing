from tkinter import *


class Settings:
    def __init__(self):
        self.language_options = [
            "Русский",
            "English"
        ]
        self.language_selected = StringVar()
        self.language_selected.set(self.language_options[0])

    def setup_option_menu(self):
        OptionMenu(self.root, self.language_selected, *self.language_options).pack()

    def setup_master(self):
        self.root.title("Settings")
        self.root.geometry("600x200")

    def add_language_label(self):
        self.label = Label(text=self.language_selected.get(),
                           width=5,
                           height=5
                           )
        self.label.pack(side=BOTTOM)

    def run(self):
        self.root = Tk()
        self.setup_master()
        self.setup_option_menu()
