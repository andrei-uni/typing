from tkinter import *


class Settings(Tk):
    def __init__(self, language, main_class):
        super().__init__()
        self.save_btn = None
        self.focus_set()
        self.attributes("-topmost", True)

        self.last_language = language
        self.withdraw()
        self.main = main_class
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
        self.save_btn = Button(self, text="Сохранить", command=self.save_closing)
        self.save_btn.grid(column=3, padx=120, pady=70)

    def setup_master(self):
        self.title("Настройки")
        self.geometry("450x200")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_language_label(self):
        self.label.pack(side=BOTTOM)
        self.label.config(text=self.language_selected.get())

    def save_closing(self):
        self.on_closing(save=True)

    def on_closing(self, save=False):
        if save:
            if self.last_language != self.language_selected.get():
                self.main.restart()
            else:
                self.withdraw()
                self.update_language_label()
                self.setting_on = False
        else:
            self.language_selected.set(self.last_language)
            self.withdraw()
            self.setting_on = False

    def run(self):
        self.last_language = self.language_selected.get()
        self.deiconify()
