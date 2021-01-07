#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

from tkcalendar import Calendar, DateEntry


class TimePicker(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.hour_spinbox = ttk.Spinbox(self, from_ = 0, to = 23, width = 2,
                                        wrap = "true", format = "%02.f",
                                        increment = 1)
        self.hour_spinbox.grid(row = 0, column = 0)
        self.minute_spinbox = ttk.Spinbox(self, from_ = 0, to = 59, width = 2,
                                        wrap = "true", format = "%02.f",
                                        increment = 1)
        self.minute_spinbox.grid(row = 0, column = 1)

#def example1():
#    def print_sel():
#        print(cal.selection_get())

#    top = tk.Toplevel(root)

#    cal = Calendar(top,
#                   font="Arial 14", selectmode='day',
#                   cursor="hand1", year=2018, month=2, day=5)
#    cal.pack(fill="both", expand=True)
#    ttk.Button(top, text="ok", command=print_sel).pack()

#def example2():
#    def print_sel():
#        print(str(cal.get()))
#        
#        
#    top = tk.Toplevel(root)

#    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

#    cal = DateEntry(top, width=12, background='darkblue',
#                    foreground='white', borderwidth=2)
#    cal.pack(padx=10, pady=10)
#    
#    but = ttk.Button(top, text = "print", command=print_sel).pack()

#root = tk.Tk()
#s = ttk.Style(root)
#s.theme_use('clam')

#ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
#ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)

#root.mainloop()

#import tkinter as tk

#class App(tk.Frame):
#    def __init__(self, parent):
#        super().__init__(parent)
#        self.hourstr=tk.StringVar(self,'10')
#        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
#        self.minstr=tk.StringVar(self,'30')
#        self.minstr.trace("w",self.trace_var)
#        self.last_value = ""
#        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
#        self.hour.grid()
#        self.min.grid(row=0,column=1)

#    def trace_var(self,*args):
#        if self.last_value == "59" and self.minstr.get() == "0":
#            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
#        self.last_value = self.minstr.get()

#root = tk.Tk()
#App(root).pack()
#root.mainloop()
