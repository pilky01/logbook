#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkcal

import logbook_db as db


def record_window(source):#, datalist):
    record_window = tk.Tk()
    record_window.title(source)
    record_frame = RecordWindow(record_window)
    record_frame.pack()

def select_window(source):
    select_window = tk.Tk()
    title_str = str("Select " + source + "...")
    select_window.title(title_str)
    select_frame = SelectWindow(select_window)
    select_frame.pack()

def search_selection(term):
    pass


class Application(ttk.Frame):

    def __init__(self, master= None, *args, **kwargs):
        super().__init__(master = master)
        self.pack()
        self.config(width = 680)
        self.create_application()
        
    def create_application(self):
        pass


class Taskbar(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master = master)
        self.create_buttons()

    def create_buttons(self):
        self.view_dashboard = ttk.Button(self, text = "Dashboard View")
        self.view_dashboard.pack()
        self.view_flightlist = ttk.Button(self, text = "Flight List View")
        self.view_flightlist.pack()
        
        self.function_newrecord = ttk.Button(self, text = "New Record",
                       command = lambda: record_window(source = "New Flight"))
        self.function_newrecord.pack()


class Dashboard(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master = master)
        

class RecordWindow(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master = master)
        self.create_record_widgets()
        
    def create_record_widgets(self):
        self.field_frame = ttk.Frame(self)
        self.field_frame.pack()
        self.origin_label = ttk.Label(self, text = "Origin Airport")
        self.origin_label.pack()
        self.origin_entry = ttk.Entry(self, state = "readonly")
        self.origin_entry.pack()
        self.origin_select = ttk.Button(self, text = "Select...",
                           command = lambda: select_window(source = "origin"))
        self.origin_select.pack()
#        self.date
        self.save_button = ttk.Button(self, text = "Save")
        self.save_button.pack()
        self.cancel_button = ttk.Button(self, text = "Cancel")
        self.cancel_button.pack()


class SelectWindow(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master = master)
        self.create_select_widgets()
    
    def create_select_widgets(self):
        self.select_entry = ttk.Entry(self)
        self.select_entry.pack()
        self.select_button = ttk.Button(self, text = "Search", 
                  command = lambda: search_selection(self.select_entry.get()))
        self.select_button.pack()
        self.select_list = ttk.Scrollbar(self)
        self.select_list.pack()

