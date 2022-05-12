from tkinter import *
from ctypes import windll
import random
import time

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.attributes('-fullscreen', True)
root["bg"] = "#54c6ff"
root.title('Tkinter Window Demo')

button = Button(text="Выключить", width=15, height=5, bg="grey", fg="white", command=root.destroy)
button.pack(side=BOTTOM)


def get_text():
    number = random.randrange(1, 9)
    with open("Texts/" + str(number) + ".txt", 'r', encoding="utf-8") as f:
        return f.read()


def calculate_correctness_percentage():
    global mistook_times, cur_index
    if cur_index == 0:
        return 0
    return (cur_index - mistook_times) / cur_index * 100


def key_pressed(event):
    global text_len, text_content, cur_index, main_text, mistook_times, correctness_percentage,\
        mistook_letter, percentage_label, char_per_minutes, start_time
    if cur_index == 0:
        start_time = time.time()
    if event.char == "":
        return
    main_text.config(state=NORMAL)
    if event.char == text_content[cur_index]:
        mistook_letter = False
        cur_index += 1
        main_text.tag_add("current", f"1.{cur_index}", f"1.{cur_index + 1}")
        main_text.tag_add("previous", f"1.0", f"1.{cur_index}")
        if cur_index != 0:
            char_per_minutes = int((cur_index / (time.time() - start_time)) * 60)
            speed_rate_label.config(text=get_speed_rate_text_template(char_per_minutes))
    else:
        if not mistook_letter:
            mistook_times += 1
            mistook_letter = True
        main_text.tag_add("wrong", f"1.{cur_index}", f"1.{cur_index + 1}")

    main_text.config(state=DISABLED)

    correctness_percentage = int(calculate_correctness_percentage())
    percentage_label.config(text=get_accuracy_text_template(correctness_percentage))


def get_accuracy_text_template(percentage):
    return f"Точность:\n {percentage}%"

def get_speed_rate_text_template(rate):
    return f"Скорость:\n {rate} зн./мин"


cur_index = 0
text_content = get_text()
text_len = len(text_content)

mistook_times = 0
correctness_percentage = 100
mistook_letter = False

percentage_label = Label(
    text=get_accuracy_text_template(correctness_percentage),
    width=10,
    height=10,
)
percentage_label.pack(side=LEFT)

main_text = Text(
    root,
    font=("Consolas", 14)
)

char_per_minutes = 0

speed_rate_label = Label(text=get_speed_rate_text_template(char_per_minutes),
                         width=10,
                         height=10)

speed_rate_label.pack(side=RIGHT)

main_text.insert(INSERT, text_content)
main_text.tag_config("current", background="green", foreground="white")
main_text.tag_config("previous", background="white", foreground="green")
main_text.tag_config("wrong", foreground="red")

main_text.tag_add("current", f"1.{cur_index}", f"1.{cur_index + 1}")
main_text.config(state=DISABLED)
main_text.pack(ipadx=10, ipady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
