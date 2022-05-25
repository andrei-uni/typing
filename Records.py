from pathlib import Path
from tkinter import *
from tkinter import ttk
from RecordType import RecordType


class Records(Tk):
    FILENAME = 'records.txt'

    def __init__(self):
        super().__init__()
        self.setup_master()
        self.withdraw()
        self.records_on = False

        self.main_frame = None

        self.setup_table()

        self.set_records_from_file()

    def setup_master(self):
        self.title("Рекорды")
        self.geometry("800x500")
        self.focus_set()
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.withdraw()
        self.records_on = False

    def setup_table(self):
        columns = ('time', 'speed', 'accuracy', 'date', 'text')
        self.main_frame = ttk.Treeview(self, columns=columns)
        self.main_frame['show'] = 'headings'

        for i in columns:
            self.main_frame.heading(i, text=i.capitalize(), anchor=CENTER)
            self.main_frame.column(i, width=130, anchor=CENTER)

        self.main_frame.pack()

    def set_records_from_file(self):
        path = Path(self.FILENAME)
        if not path.exists():
            return

        with path.open("r") as f:
            for line in f.readlines():
                self.main_frame.insert('', 'end', values=line.split(","))

    def add_new_record(self, record: RecordType):
        path = Path(self.FILENAME)
        if not path.exists():
            path.touch(mode=0o644)

        with path.open("a+") as f:
            values = [str(i) for i in vars(record).values()]
            print(",".join(values), file=f)

    def run(self):
        self.deiconify()
