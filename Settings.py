from tkinter import *


class Settings:
    def __init__(self, language):
        self.root = Tk()
        self.root.withdraw()
        self.language_options = [
            "Русский",
            "English"
        ]
        self.language_selected = StringVar()
        self.language_selected.set(language)
        self.label = Label(text=self.language_selected.get())
        self.label.pack(side=BOTTOM)
        self.setting_on = False
        self.setup_option_menu()
        self.setup_master()

    def setup_option_menu(self):
        OptionMenu(self.root, self.language_selected, *self.language_options).pack()

    def setup_master(self):
        self.root.title("Settings")
        self.root.geometry("600x200")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_language_label(self):
        self.label.pack(side=BOTTOM)
        self.label.config(text=self.language_selected.get())

    def on_closing(self):
        self.root.withdraw()
        self.update_language_label()
        self.setting_on = False

    def run(self):
        self.root.deiconify()
