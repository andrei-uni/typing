from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog


class Settings:
    def __init__(self, language, main_class):
        self.main = main_class
        self.root = Toplevel(main_class.root)

        self.choose_color_button = None
        self.open_file_button = None
        self.save_button = None

        self.last_language = language
        self.languages = ('Русский', 'English')
        self.language_selected = StringVar(self.root)
        self.language_selected.set(language)

        self.label = Label(text=f"Текущий язык: {self.language_selected.get()}")
        self.label.pack(side=BOTTOM)
        self.setup_master()
        self.create_widgets()

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}
        label = Label(self.root, text='Язык:')
        label.grid(column=0, row=0, sticky=W, **paddings)

        option_menu = OptionMenu(
            self.root,
            self.language_selected,
            *self.languages
        )

        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        self.save_button = Button(self.root, text="Сохранить", command=self.save_closing)
        self.save_button.place(x=330, y=140)
        self.switch_music = Button(self.root, text="Звук", command=self.main.off_music)
        self.switch_music.place(x=200, y=100)

        self.choose_color_button = Button(self.root, text="Выберите цвет", command=self.onChoose)
        self.choose_color_button.place(x=10, y=140)

        self.open_file_button = Button(self.root, text="Выбрать файл", command=self.choose_file)
        self.open_file_button.place(x=140, y=140)

    def onChoose(self):
        self.main.bg = colorchooser.askcolor()[1]

    def choose_file(self):
        filetypes = (
            ('text files', '*.txt'),
        )

        filename = filedialog.askopenfilename(
            title='Выберите файл',
            initialdir='/',
            filetypes=filetypes
        )

        if filename == '':
            self.main.restart()
        else:
            self.main.restart(filename)

    def setup_master(self):
        self.root.title("Настройки")
        self.root.geometry("450x200")
        self.root.focus_set()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.withdraw()

    def update_language_label(self):
        self.label.pack(side=BOTTOM)
        self.label.config(text=f"Текущий язык: {self.language_selected.get()}")

    def save_closing(self):
        self.on_closing(save=True)

    def on_closing(self, save=False):
        if save:
            self.main.root['bg'] = self.main.bg
            if self.last_language != self.language_selected.get():
                self.main.restart()
            else:
                self.root.withdraw()
                self.update_language_label()
        else:
            self.language_selected.set(self.last_language)
            self.root.withdraw()
        self.root.grab_release()

    def run(self):
        self.last_language = self.language_selected.get()
        self.root.deiconify()
        self.root.grab_set()
