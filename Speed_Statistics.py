import time
from tkinter import *


class Statistics:
    def __init__(self, length):
        self.length = length
        self.cur_index = 0
        self.rate = 0
        self.start_time = None
        self.label = None

    def get_speed_rate_text_template(self):
        return f"Скорость:\n {self.rate} зн./мин"

    def add_statistic_in_app(self, side):
        self.label = Label(text=self.get_speed_rate_text_template(),
                  width=10,
                  height=10,)
        self.label.pack(side=side)

    def update_statistic(self):
        self.cur_index += 1
        self.rate = self.calculate_speed()
        self.label.config(text=self.get_speed_rate_text_template())

    def calculate_speed(self):
        return int((self.cur_index / (time.perf_counter() - self.start_time)) * 60)
