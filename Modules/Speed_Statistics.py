import math
import time
from tkinter import *


class SpeedStatistics:

    def __init__(self):
        self.cur_index = 0
        self.rate = 0
        self.start_time = None
        self.label = None

    def get_speed_rate_text_template(self):
        return f"Скорость:\n {self.rate} зн./мин"

    def start_timer(self):
        self.cur_index = 0
        self.start_time = time.perf_counter()

    def add_statistic_in_app(self):
        self.label = Label(text=self.get_speed_rate_text_template(), width=10, height=10)
        self.label.place(x=1815, y=700)

    def update_statistic(self):
        self.cur_index += 1
        self.rate = self.calculate_speed(self.cur_index, self.start_time)
        self.label.config(text=self.get_speed_rate_text_template())

    @staticmethod
    def calculate_speed(cur_index, start_time):
        return math.ceil(cur_index / (time.perf_counter() - start_time) * 60)



