import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('300x200+50+50')
root.resizable(False, False)
root.title('Tkinter Window Demo')


def get_text():
    with open("text.txt", 'r') as f:
        return f.read()


def key_pressed(event):
    global text, cur_index, label
    if event.char == text[cur_index]:
        cur_index += 1
        label.config(text=text[cur_index:cur_index + symbols_at_a_time])


cur_index = 0
symbols_at_a_time = 10
text = get_text()


label = ttk.Label(
    root,
    text=text[cur_index:symbols_at_a_time],
    font=("Helvetica", 14)
)
label.pack(ipadx=10, ipady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
