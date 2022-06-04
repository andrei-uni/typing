import random
import datetime
import time
import platform
import pygame

from tkinter import *
from pathlib import Path

import Accuracy_Statistics as ac
import Speed_Statistics as sp
import Settings as st
import Records as rec
from RecordType import RecordType


class CurrentSettings:
    language = "Русский"
    bg = "#54c6ff"

    available_languages = ('Русский', 'English')


CURRENT_SETTINGS = CurrentSettings()


class Application:
    def __init__(self, custom_file=''):
        self.root = Tk()
        self.setup_root()

        self.cur_index = 0
        self.filename = None

        self.off_button = None
        self.settings_button = None
        self.restart_btn = None
        self.records_button = None

        self.settings = st.Settings(self, CURRENT_SETTINGS)
        self.records = rec.Records(self)
        self.speed_stat = sp.Statistics()
        self.accuracy_stat = ac.Statistic(self)

        if custom_file == '':
            self.text = self.open_preset_file(CURRENT_SETTINGS.language)
        else:
            self.text = self.open_custom_file(custom_file)

        self.text_widget = Text(self.root, font=("Consolas", 14), bg="white", fg='#2a2a2a', insertontime=0)
        self.setup_text_widget()

        self.text_len = len(self.text)

        self.add_buttons()

        self.current_language_label = Label(text=f"Текущий язык: {CURRENT_SETTINGS.language}")
        self.current_language_label.pack(side=BOTTOM)
        self.root.focus_force()

    def setup_root(self):
        self.root.attributes('-fullscreen', True)
        self.set_bg()
        self.root.title("Клавиатурный тренажер")
        self.root.bind("<Key>", self.key_pressed)

    def setup_text_widget(self):
        self.text_widget.insert(INSERT, self.text)
        self.text_widget.tag_config("current", background="green", foreground="white")
        self.text_widget.tag_config("previous", background="white", foreground="green")
        self.text_widget.tag_config("wrong", foreground="red")
        self.text_widget.config(state=DISABLED)
        self.text_widget.pack(ipadx=10, ipady=10)
        self.add_highlight_for_symbol("current", self.cur_index, self.cur_index + 1)

        self.accuracy_stat.add_statistic_in_app(LEFT)
        self.speed_stat.add_statistic_in_app(RIGHT)

    def add_highlight_for_symbol(self, name, first, second):
        self.text_widget.tag_add(name, f"1.{first}", f"1.{second}")

    def add_record(self):
        self.records.add_new_record(RecordType(f'{int(time.perf_counter() - self.speed_stat.start_time)} сек.',
                                               self.speed_stat.rate,
                                               self.accuracy_stat.percent,
                                               datetime.datetime.today().strftime('%d.%m.%y %H:%M:%S'),
                                               self.filename
                                               )
                                    )

    def key_pressed(self, event):
        if event.char == "" or self.cur_index == self.text_len:
            return

        if self.cur_index == 0:
            self.speed_stat.start_timer()

        if event.char == self.text[self.cur_index]:
            if not self.accuracy_stat.mistook_letter:
                self.accuracy_stat.correct_times += 1
            self.accuracy_stat.mistook_letter = False
            self.cur_index += 1
            self.add_highlight_for_symbol("current", self.cur_index, self.cur_index + 1)
            self.add_highlight_for_symbol("previous", self.cur_index - 1, self.cur_index)
            if self.cur_index != 1:
                self.speed_stat.update_statistic()
        else:
            if not self.accuracy_stat.mistook_letter:
                self.accuracy_stat.mistook_letter = True
            self.add_highlight_for_symbol("wrong", self.cur_index, self.cur_index + 1)

        if self.cur_index == self.text_len:
            self.add_record()

        self.accuracy_stat.update_statistic()

    def open_preset_file(self, lang):
        if lang == "Русский":
            sel_lang = "ru"
        elif lang == "English":
            sel_lang = "en"
        else:
            raise Exception("Incorrect Language")

        files = [i for i in Path("Texts", sel_lang).iterdir()]
        self.filename = random.choice(files)

        return self.open_file(self.filename)

    def open_custom_file(self, file):
        self.filename = file
        return self.open_file(Path(file))

    def open_file(self, file: Path):
        with file.open(encoding="utf-8") as f:
            return f.read().strip()

    def on_music(self):
        pygame.mixer.music.unpause()
        self.settings.switch_music['command'] = self.off_music
        self.settings.switch_music['text'] = 'Выключить музыку'

    def off_music(self):
        self.settings.switch_music['command'] = self.on_music
        self.settings.switch_music['text'] = 'Включить музыку'
        pygame.mixer.music.pause()

    def set_bg(self):
        self.root["bg"] = CURRENT_SETTINGS.bg

    def close(self):
        self.settings.root.destroy()
        self.records.root.destroy()
        self.root.destroy()

    def restart(self, custom_file=''):
        self.close()
        Application(custom_file).run()

    def add_buttons(self):
        self.off_button = Button(self.root, text="Выключить", bg="grey", fg="white", command=self.close)
        self.off_button.place(x=910, y=1000)

        self.settings_button = Button(self.root, text="Настройки", command=self.settings.run)
        self.settings_button.place(x=890, y=820)

        self.records_button = Button(self.root, text="Рекорды", command=self.records.run)
        self.records_button.place(x=795, y=820)

        self.restart_btn = Button(self.root, text="Перезапустить", command=self.restart)
        self.restart_btn.place(x=1000, y=820)

    def run(self):
        self.root.mainloop()


def add_music():
    pygame.init()
    music_dir = Path("Music")
    tracks = [i for i in music_dir.iterdir()]
    pygame.mixer.music.load(random.choice(tracks))
    for music in tracks:
        pygame.mixer.music.queue(music)
    pygame.mixer.music.play()


if __name__ == "__main__":
    if platform.system() == "Windows":
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    add_music()
    Application().run()
