from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

from App import CurrentSettings


class Settings:
    def __init__(self, main_class, current_settings: CurrentSettings):
        self.main = main_class
        self.CURRENT_SETTINGS = current_settings
        self.root = Toplevel(main_class.root)

        self.switch_music_button = None
        self.choose_color_button = None
        self.open_file_button = None
        self.save_button = None

        self.current_language = current_settings.language
        self.chosen_color = current_settings.bg

        self.language_selected = StringVar(self.root)
        self.language_selected.set(current_settings.language)

        self.setup_master()
        self.create_widgets()

    def create_widgets(self):
        paddings = {'padx': 5, 'pady': 5}
        label = Label(self.root, text='Язык:')
        label.grid(column=0, row=0, sticky=W, **paddings)

        option_menu = OptionMenu(
            self.root,
            self.language_selected,
            *self.CURRENT_SETTINGS.available_languages
        )

        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        self.save_button = Button(self.root, text="Сохранить", command=self.save_closing)
        self.save_button.place(x=330, y=140)

        self.switch_music_button = Button(self.root, text="Звук", command=self.main.off_music)
        self.switch_music_button.place(x=200, y=100)

        self.choose_color_button = Button(self.root, text="Выберите цвет", command=self.on_color_chosen)
        self.choose_color_button.place(x=10, y=140)

        self.open_file_button = Button(self.root, text="Выбрать файл", command=self.choose_file)
        self.open_file_button.place(x=140, y=140)

    def on_color_chosen(self):
        self.chosen_color = colorchooser.askcolor()[1]

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

    def save_closing(self):
        self.on_closing(save=True)

    def on_closing(self, save=False):
        if save:
            self.CURRENT_SETTINGS.bg = self.chosen_color
            self.main.set_bg()

            if self.current_language == self.language_selected.get():
                self.root.withdraw()
            else:
                self.CURRENT_SETTINGS.language = self.language_selected.get()
                self.main.restart()
        else:
            self.chosen_color = self.CURRENT_SETTINGS.bg
            self.language_selected.set(self.current_language)

            self.root.withdraw()

        self.root.grab_release()

    def run(self):
        self.root.deiconify()
        self.root.grab_set()
