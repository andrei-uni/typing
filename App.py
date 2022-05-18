from tkinter import *
from ctypes import windll
import random
import time
import Speed_statistic as sp
import Accuracy as ac

windll.shcore.SetProcessDpiAwareness(1)


class Application:

    def __init__(self, text):
        self.text = text
        self.root = Tk()
        self.cur_index = 0
        self.text_len = len(text)
        self.main_text = Text(self.root,
                              font=("Consolas", 14))
        self.speed_stat = sp.Statistic(self.text_len)
        self.accuracy_stat = ac.Statistic(self.text_len)

    def setup_root(self):
        self.root.attributes('-fullscreen', True)
        self.root["bg"] = "#54c6ff"
        self.root.title('Tkinter Window Demo')
        self.root.bind("<Key>", self.key_pressed)

    def setup_frame(self):
        self.main_text.insert(INSERT, self.text)
        self.main_text.tag_config("current", background="green", foreground="white")
        self.main_text.tag_config("previous", background="white", foreground="green")
        self.main_text.tag_config("wrong", foreground="red")
        self.main_text.config(state=DISABLED)
        self.main_text.pack(ipadx=10, ipady=10)
        self.add_highlight_for_symbol("current", self.cur_index, self.cur_index + 1)

    def add_highlight_for_symbol(self, name, first, second):
        self.main_text.tag_add(name, f"1.{first}", f"1.{second}")

    def key_pressed(self, event):
        if event.char == "" or self.cur_index == self.text_len:
            return
        if self.cur_index == 0:
            self.speed_stat.start_time = time.perf_counter()
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

    def start(self):
        self.setup_root()
        self.setup_frame()
        self.accuracy_stat.add_statistic_in_app(LEFT)
        self.speed_stat.add_statistic_in_app(RIGHT)
        self.root.mainloop()


if __name__ == "__main__":

    app = Application("Эта книга адресована")
    app.start()
