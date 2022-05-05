import tkinter as tk
from tkinter import ttk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width / 2
window_height = screen_height / 2
horiz_pad = screen_width / 2 - window_width / 2
vert_pad = screen_height / 2 - window_height / 2
root.geometry(f'{int(window_width)}x{int(window_height)}+{int(horiz_pad)}+{int(vert_pad)}')
root.resizable(True, True)
root.attributes('-fullscreen', True)
root.title('Tkinter Window Demo')

button = tk.Button(text="Выключить", width=15, height=5, bg="grey", fg="white", command=root.destroy)
button.pack(side=tk.BOTTOM)


def get_text():
    with open("text.txt", 'r') as f:
        return f.read()


def key_pressed(event):
    global text, cur_index, label
    if event.char == text[cur_index]:
        cur_index += 1
        label.config(text=text[cur_index:])


cur_index = 0
text = get_text()

label = ttk.Label(
    root,
    text=text[cur_index:],
    font=("Helvetica", 14)
)
label.pack(ipadx=10, ipady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
