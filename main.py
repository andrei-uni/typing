from tkinter import *
from ctypes import windll
import random
import time

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()


def setup_root():
    global root
    root.attributes('-fullscreen', True)
    root["bg"] = "#54c6ff"
    root.title('Tkinter Window Demo')


def add_button(text, width, height, bg, fg, command, side):
    button = Button(text=text, width=width, height=height, bg=bg, fg=fg, command=command)
    button.pack(side=side)
    return button


def get_text():
    number = random.randrange(1, 9)
    with open("Texts/" + str(number) + ".txt", 'r', encoding="utf-8") as f:
        return f.read()


def create_frame():
    main_text = Text(root,
                     font=("Consolas", 14))

    main_text.insert(INSERT, text_content)
    main_text.tag_config("current", background="green", foreground="white")
    main_text.tag_config("previous", background="white", foreground="green")
    main_text.tag_config("wrong", foreground="red")
    main_text.config(state=DISABLED)
    main_text.pack(ipadx=10, ipady=10)

    return main_text


def get_accuracy_text_template(percentage):
    return f"Точность:\n {percentage}%"


def get_speed_rate_text_template(rate):
    return f"Скорость:\n {rate} зн./мин"


def calculate_correctness_percentage():
    global mistook_times, cur_index
    if cur_index == 0:
        return 0
    return (cur_index - mistook_times) / cur_index * 100


def add_tag(name, first, second):
    global main_text
    main_text.tag_add(name, f"1.{first}", f"1.{second}")


def key_pressed(event):
    global cur_index, mistook_times, mistook_letter, start_time
    if cur_index == 0:
        start_time = time.perf_counter()
    if event.char == "" or cur_index == text_len:
        return
    main_text.config(state=NORMAL)
    if event.char == text_content[cur_index]:
        # mistook_letter = False
        cur_index += 1
        add_tag("current", cur_index, cur_index + 1)
        add_tag("previous", cur_index - 1, cur_index)
        if cur_index != 0:
             char_per_minutes = int((cur_index / (time.perf_counter() - start_time)) * 60)
             speed_rate_label.config(text=get_speed_rate_text_template(char_per_minutes))
    else:
        if not mistook_letter:
            mistook_times += 1
            mistook_letter = True
        add_tag("wrong", cur_index, cur_index + 1)

    main_text.config(state=DISABLED)

    correctness_percentage = int(calculate_correctness_percentage())
    percentage_label.config(text=get_accuracy_text_template(correctness_percentage))


def create_statistic(text, value, side):
    label = Label(text=text(value),
                  width=10,
                  height=10, )
    label.pack(side=side)
    return label

setup_root()
button = add_button(text="Выключить", width=15, height=5, bg="grey", fg="white", command=root.destroy, side=BOTTOM)

cur_index = 0
text_content = get_text()
text_len = len(text_content)
char_per_minutes = 0

mistook_times = 0
correctness_percentage = 100
mistook_letter = False

percentage_label = create_statistic(get_accuracy_text_template, correctness_percentage, side=LEFT)

speed_rate_label = create_statistic(get_speed_rate_text_template, char_per_minutes, side=RIGHT)

main_text = create_frame()

add_tag("current", cur_index, cur_index + 1)

root.bind("<Key>", key_pressed)

root.mainloop()
