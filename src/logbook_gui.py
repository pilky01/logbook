#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkcal

import logbook_db as db


class Application(ttk.Frame):

    def __init__(self, master= None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack()
        self.config(width = 680)
        self.create_application()
        
    def create_application(self):
        pass


class Taskbar(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_buttons()

    def create_buttons(self):
        self.view_dashboard = ttk.Button(self, text = "Dashboard View")
        self.view_dashboard.pack()
        self.view_flightlist = ttk.Button(self, text = "Flight List View")
        self.view_flightlist.pack()
        self.function_newrecord = ttk.Button(self, text = "New Record",
                                   command = lambda: self.new_flight_record())
        self.function_newrecord.pack()
        
    def new_flight_record(self):
        record_window = FlightRecordWindow(self)
        record_window.title("New Flight")


class Dashboard(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class BaseRecordWindow(tk.Toplevel):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_base_widgets()
    
    def create_base_widgets(self):
        self.field_frame = ttk.Frame(self)
        self.field_frame.pack()
      
class FlightRecordWindow(BaseRecordWindow):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_record_widgets()
        
    def create_record_widgets(self):
        self.origin_label = ttk.Label(self, text = "Origin Airport")
        self.origin_label.pack()
        self.origin_entry = ttk.Entry(self, state = "readonly")
        self.origin_entry.pack()
        self.origin_select = ttk.Button(self, text = "Select...",
                            command = lambda: self.origin_select_window())
        self.origin_select.pack()
#        self.date
        self.save_button = ttk.Button(self, text = "Save")
        self.save_button.pack()
        self.cancel_button = ttk.Button(self, text = "Cancel")
        self.cancel_button.pack()
        
    def origin_select_window(self):
    ##need to select class of SelectWindow
        origin_select_window = OriginSelectWindow(self, source = "origin")
        origin_select_window.title("Select Origin...")
        origin_select_window.geometry("500x350")

class BaseSelectWindow(tk.Toplevel):
    
    def __init__(self, master = None, source = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source = source
        self.search_results = []
        self.create_base_widgets()
    
    def create_base_widgets(self):
        # input frame
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack()
        self.select_entry = ttk.Entry(self.input_frame)
        self.select_entry.pack()
        self.select_button = ttk.Button(self.input_frame, text = "Search", 
                                       command = lambda: self.search_update())
        self.select_button.pack()
        # results
        self.select_list = tk.Listbox(self)
        self.select_list.pack()
        # result info
        self.info_frame = ttk.Frame(self)
        self.info_frame.pack()
    
    def search_update(self):
        self.select_list.delete(0, tk.END)
        self.search_results = db.search_selection(self.select_entry.get(),
                                                  self.source)
        for result in self.search_results:
            self.select_list.insert(tk.END, result[1])
        print(self.search_results)


class OriginSelectWindow(BaseSelectWindow):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_custom_widgets()
    
    def create_custom_widgets(self):
        self.name_label_var = tk.StringVar()
        self.name_label = ttk.Label(self.info_frame,
                                    text = self.name_label_var).pack()
        self.icaocode_label_var = tk.StringVar()
        self.icaocode_label = ttk.Label(self.info_frame,
                                        text = self.icaocode_label_var).pack()
        self.iatacode_label_var = tk.StringVar()
        self.iatacode_label = ttk.Label(self.info_frame,
                                        text = self.iatacode_label_var).pack()
