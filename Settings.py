from tkinter import *


class Settings(Tk):
    def __init__(self, language):
        super().__init__()
        self.withdraw()
        self.languages = ('Русский', 'English')
        self.language_selected = StringVar(self)
        self.language_selected.set(language)

        self.label = Label(text=self.language_selected.get())
        self.label.pack(side=BOTTOM)
        self.setting_on = False
        self.setup_master()
        self.create_widgets()

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}
        label = Label(self, text='Язык:')
        label.grid(column=0, row=0, sticky=W, **paddings)

        option_menu = OptionMenu(
            self,
            self.language_selected,
            *self.languages
        )

        option_menu.grid(column=1, row=0, sticky=W, **paddings)

    def setup_master(self):
        self.title("Настройки")
        self.geometry("600x200")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_language_label(self):
        self.label.pack(side=BOTTOM)
        self.label.config(text=self.language_selected.get())

    def on_closing(self):
        self.withdraw()
        self.update_language_label()
        self.setting_on = False

    def run(self):
        self.deiconify()
