from pathlib import Path
from tkinter import *
from tkinter import ttk
import Modules.RecordType


class Records():
    FILENAME = '../records.txt'

    def __init__(self, main_class):
        self.root = Toplevel(main_class.root)
        self.setup_master()
        self.root.withdraw()

        self.main_frame = None

        self.setup_table()
        self.set_records_from_file()

    def setup_master(self):
        self.root.title("Рекорды")
        self.root.geometry("1200x500")
        self.root.focus_set()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.root.withdraw()
        self.root.grab_release()

    def setup_table(self):
        columns = ('time', 'speed', 'accuracy', 'date', 'text')
        self.main_frame = ttk.Treeview(self.root, columns=columns)
        self.main_frame['show'] = 'headings'

        for i in columns:
            self.main_frame.heading(i,
                                    text=i.capitalize(), anchor=CENTER,
                                    command=lambda _col=i: self.sort_treeview(_col, True)
                                    )
            self.main_frame.column(i, width=200, anchor=CENTER)

        self.main_frame.pack()

    def set_records_from_file(self):
        path = Path(self.FILENAME)
        if not path.exists():
            return

        with path.open("r") as f:
            for line in f.readlines():
                self.main_frame.insert('', 'end', values=line.split(","))

    def add_new_record(self, record: Modules.RecordType):
        path = Path(self.FILENAME)
        if not path.exists():
            path.touch(mode=0o644)

        with path.open("a+") as f:
            values = [str(i) for i in vars(record).values()]
            value = ",".join(values)
            print(value, file=f)
            self.main_frame.insert('', 'end', values=value.split(","))

    def sort_treeview(self, column, reverse: bool):
        try:
            data_list = [(int(self.main_frame.set(k, column)), k) for k in self.main_frame.get_children("")]
        except Exception:
            data_list = [(self.main_frame.set(k, column), k) for k in self.main_frame.get_children("")]

        data_list.sort(reverse=reverse)

        for index, (val, k) in enumerate(data_list):
            self.main_frame.move(k, "", index)

        self.main_frame.heading(
            column=column,
            text=column.title(),
            command=lambda _col=column: self.sort_treeview(_col, not reverse)
        )

    def run(self):
        self.root.deiconify()
        self.root.grab_set()
