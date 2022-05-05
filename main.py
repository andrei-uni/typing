from tkinter import *


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width / 2
window_height = screen_height / 2
horiz_pad = screen_width / 2 - window_width / 2
vert_pad = screen_height / 2 - window_height / 2
root.geometry(f'{int(window_width)}x{int(window_height)}+{int(horiz_pad)}+{int(vert_pad)}')
root.resizable(False, False)
root.title('Tkinter Window Demo')


def get_text():
    with open("text.txt", 'r') as f:
        return f.read()


def key_pressed(event):
    global text_content, cur_index, text
    if event.char == text_content[cur_index]:
        cur_index += 1
        text.config(state=NORMAL)
        text.delete("1.0", "end")
        text.insert(INSERT, text_content[cur_index:])
        text.config(state=DISABLED)


cur_index = 0
text_content = get_text()


text = Text(
    root,
    font=("Helvetica", 14)
)
text.insert(INSERT, text_content[cur_index:])
text.config(state=DISABLED)
text.pack(ipadx=10, ipady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
