from tkinter import *


root = Tk()
root.attributes('-fullscreen', True)
root.title('Tkinter Window Demo')

button = Button(text="Выключить", width=15, height=5, bg="grey", fg="white", command=root.destroy)
button.pack(side=BOTTOM)


def get_text():
    with open("text.txt", 'r') as f:
        return f.read()


def key_pressed(event):
    global text_content, cur_index, text
    if event.char == text_content[cur_index]:
        cur_index += 1
        text.config(state=NORMAL)
        text.tag_add("current", f"1.{cur_index}", f"1.{cur_index+1}")
        text.tag_add("previous", f"1.0", f"1.{cur_index}")
        text.config(state=DISABLED)


cur_index = 0
text_content = get_text()


text = Text(
    root,
    font=("Helvetica", 14)
)
text.insert(INSERT, text_content)
text.tag_config("current", background="green", foreground="white")
text.tag_config("previous", background="white", foreground="green")
text.tag_add("current", f"1.{cur_index}", f"1.{cur_index+1}")
text.config(state=DISABLED)
text.pack(ipadx=10, ipady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
