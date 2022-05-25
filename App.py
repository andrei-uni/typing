import random

from tkinter import *
from ctypes import windll
from pathlib import Path

import Accuracy_Statistics as ac
import Settings as st
import Speed_Statistics as sp


class Application:
    def __init__(self, language='Русский'):
        self.root = Tk()
        self.root.focus_force()
        self.cur_index = 0
        self.main_label = Text(self.root, font=("Consolas", 14))

        self.off_button = None
        self.settings_button = None
        self.restart_btn = None
        self.settings = st.Settings(language, self)
        self.text = self.open_file(self.settings.language_selected.get())
        self.text_len = len(self.text)

        self.speed_stat = sp.Statistics()
        self.accuracy_stat = ac.Statistic(self)

        self.setup_root()
        self.setup_frame()
        self.add_buttons()

    def setup_root(self):
        self.root.attributes('-fullscreen', True)
        self.root["bg"] = "#54c6ff"
        self.root.title("Клавиатурный тренажер")
        self.root.bind("<Key>", self.key_pressed)

    def open_settings(self):
        if not self.settings.setting_on:
            self.settings.setting_on = True
            self.settings.run()

    def setup_frame(self):
        self.main_label.insert(INSERT, self.text)
        self.main_label.tag_config("current", background="green", foreground="white")
        self.main_label.tag_config("previous", background="white", foreground="green")
        self.main_label.tag_config("wrong", foreground="red")
        self.main_label.config(state=DISABLED)
        self.main_label.pack(ipadx=10, ipady=10)
        self.add_highlight_for_symbol("current", self.cur_index, self.cur_index + 1)

        self.accuracy_stat.add_statistic_in_app(LEFT)
        self.speed_stat.add_statistic_in_app(RIGHT)

    def add_highlight_for_symbol(self, name, first, second):
        self.main_label.tag_add(name, f"1.{first}", f"1.{second}")

    def key_pressed(self, event):
        if event.char == "" or self.cur_index == self.text_len:
            return
        if self.cur_index == 0:
            self.speed_stat.start_timer()

        if event.char == self.text[self.cur_index]:
            self.accuracy_stat.mistook_letter = False
            self.cur_index += 1
            self.add_highlight_for_symbol("current", self.cur_index, self.cur_index + 1)
            self.add_highlight_for_symbol("previous", self.cur_index - 1, self.cur_index)
            if self.cur_index != 1:
                self.speed_stat.update_statistic()
        else:
            if not self.accuracy_stat.mistook_letter:
                self.accuracy_stat.mistook_times += 1
                self.accuracy_stat.mistook_letter = True
            self.add_highlight_for_symbol("wrong", self.cur_index, self.cur_index + 1)

        self.accuracy_stat.update_statistic()

    def open_file(self, lang):
        if lang == "Русский":
            sel_lang = "ru"
        elif lang == "English":
            sel_lang = "en"
        else:
            raise Exception("Incorrect Language")

        texts_dir = Path("Texts", sel_lang)
        files = [i for i in texts_dir.iterdir()]
        random_file = random.choice(files)

        with random_file.open(encoding="utf-8") as f:
            return f.read()

    def close(self):
        self.settings.destroy()
        self.root.destroy()

    def restart(self):
        language = self.settings.language_selected.get()
        self.close()
        Application(language).run()

    def add_buttons(self):
        self.off_button = Button(self.root, text="Выключить", bg="grey", fg="white", command=self.close)
        self.off_button.pack(side=BOTTOM)

        self.settings_button = Button(self.root, text="Настройки", command=self.open_settings)
        self.settings_button.pack(pady=10)

        self.restart_btn = Button(self.root, text="Перезапустить", command=self.restart)
        self.restart_btn.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    windll.shcore.SetProcessDpiAwareness(1)

    app = Application()
    app.run()
