from tkinter import *


class Statistic:
    def __init__(self, main_class):
        self.main_class = main_class
        self.correct_times = 0
        self.mistook_letter = False
        self.label = None
        self.percent = 100

    def get_accuracy_text_template(self):
        return f"Точность:\n {self.percent}%"

    def add_statistic_in_app(self, side):
        self.label = Label(text=self.get_accuracy_text_template(), width=10, height=10)
        self.label.place(x=0, y=700)

    def update_statistic(self):
        self.percent = self.calculate_correctness_percent()
        self.label.config(text=self.get_accuracy_text_template())

    def calculate_correctness_percent(self):
        if self.main_class.cur_index == 0:
            return 0
        return int(self.correct_times / self.main_class.cur_index * 100)
