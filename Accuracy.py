from tkinter import *
import time


class Statistic:

    def __init__(self, length):
        self.length = length
        self.cur_index = 0
        self.mistook_times = 0
        self.mistook_letter = False
        self.label = None
        self.percentage = 100

    def get_accuracy_text_template(self):
        return f"Точность:\n {self.percentage}%"

    def add_statistic_in_app(self, side):
        self.label = Label(text=self.get_accuracy_text_template(),
                  width=10,
                  height=10,)
        self.label.pack(side=side)

    def update_statistic(self):
        self.cur_index += 1
        self.percentage = self.calculate_correctness_percentage()
        self.label.config(text=self.get_accuracy_text_template())

    def calculate_correctness_percentage(self):
        if self.cur_index == 0:
            return 0
        return int((self.cur_index - self.mistook_times) / self.cur_index * 100)



