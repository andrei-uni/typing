from tkinter import *
from ctypes import windll
import random


windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.attributes('-fullscreen', True)
root["bg"] = "#54c6ff"
root.title('Tkinter Window Demo')

button = Button(text="Выключить", width=15, height=5, bg="grey", fg="white", command=root.destroy)
button.pack(side=BOTTOM)


def get_text():
    number = random.randrange(1, 5, 1)
    with open(str(number)+".txt", 'r', encoding="utf-8") as f:
        return f.read()


def key_pressed(event):
    global text_content, cur_index, main_text
    if event.char == "":
        return
    main_text.config(state=NORMAL)
    if event.char == text_content[cur_index]:
        cur_index += 1
        main_text.tag_add("current", f"1.{cur_index}", f"1.{cur_index+1}")
        main_text.tag_add("previous", f"1.0", f"1.{cur_index}")
    else:
        main_text.tag_add("wrong", f"1.{cur_index}", f"1.{cur_index+1}")

    main_text.config(state=DISABLED)


cur_index = 0
text_content = get_text()

main_text = Text(
    root,
    font=("Consolas", 14)
)
main_text.insert(INSERT, text_content)
main_text.tag_config("current", background="green", foreground="white")
main_text.tag_config("previous", background="white", foreground="green")
main_text.tag_config("wrong", foreground="red")

main_text.tag_add("current", f"1.{cur_index}", f"1.{cur_index+1}")
main_text.config(state=DISABLED)
main_text.pack(ipadx=10, ipady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
