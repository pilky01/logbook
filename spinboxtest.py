#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk


class Application(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack()
#        self.master = master
        self.create_widgets()
        
    def create_widgets(self):
#        self.testframe = ttk.Frame(self)
#        self.testframe.pack()
#        self.testlabel = ttk.Label(self.testframe, text = "test")
#        self.testlabel.pack()
        self.testwidget = TimePicker(self)
        self.testwidget.grid(row = 0, column = 1)

class TimePicker(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
#        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.label = ttk.Label(self, text = "Testing")
        self.label.grid(row = 0, column = 0)
        self.hour_spinbox = ttk.Spinbox(self, from_ = 0, to = 23,
                                        increment = 1)#, format = "%2.0f")
        self.hour_spinbox.grid(row = 0, column = 1)
        

def main():
    root = tk.Tk()
    root.title('Logbook')
    root.geometry("600x300")

    app = Application(root)
    app.mainloop()

if __name__ == "__main__":
    main()
