from tkinter import *
from ctypes import windll
import time
import Speed_Statistics as sp
import Accuracy_Statistics as ac
import Settings as settings


class Application:
    def __init__(self, text):
        self.root = Tk()
        self.text = text
        self.cur_index = 0
        self.text_len = len(text)
        self.main_label = Text(self.root,
                               font=("Consolas", 14)
                               )
        self.speed_stat = sp.Statistics(self.text_len)
        self.accuracy_stat = ac.Statistic(self.text_len)
        self.sett = settings.Settings()

        ###############
        self.off_button = Button(text="Выключить", bg="grey", fg="white", command=self.close)
        self.btn = Button(self.root, text="Settings")
        #self.restart_btn = Button(self.root, text="Restart")
        ################

        self.setup_root()
        self.setup_frame()
        self.add_buttons()

    def setup_root(self):
        self.root.attributes('-fullscreen', True)
        self.root["bg"] = "#54c6ff"
        self.root.title('Tkinter Window Demo')
        self.root.bind("<Key>", self.key_pressed)

    def turn_on_settings(self):
        if not self.sett.setting_on:
            self.sett.setting_on = True
            return self.sett.run()

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

    def close(self):
        self.sett.root.destroy()
        self.root.destroy()

    def restart(self):
        self.root.destroy()
        Application("Эта книга адресована").run()

    def add_buttons(self):
        #self.restart_btn.bind("<Button>", lambda _: self.restart())
        self.btn.bind("<Button>", lambda _: self.turn_on_settings())
        self.btn.pack(pady=10)
        #self.restart_btn.pack()
        self.off_button.pack(side=BOTTOM)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    windll.shcore.SetProcessDpiAwareness(1)

    app = Application("Эта книга адресована")
    app.run()
