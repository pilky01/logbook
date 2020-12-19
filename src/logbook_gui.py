#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkcal

import logbook_db as db


class Application(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
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
        origin_select_window = OriginSelectWindow(self, source = "origin")
        origin_select_window.title("Select Origin...")
        #origin_select_window.geometry("500x350")

class BaseSelectWindow(tk.Toplevel):
    
    def __init__(self, master = None, source = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(padx = 5, pady = 3)
        self.source = source
        self.search_results = []
        self.create_base_widgets()
    
    def create_base_widgets(self):
        #frames
        self.input_frame = ttk.Frame(self, padding = 2)
        self.input_frame.grid(row = 0, column = 0, columnspan = 2,
                              sticky = "nsew")
        self.select_list_frame = ttk.Frame(self, padding = 2)
        self.select_list_frame.grid(row = 1, column = 0, rowspan = 2,
                                    columnspan = 1, sticky = "nsew")
        self.info_frame = ttk.Frame(self, borderwidth = 2, padding = 2)
        self.info_frame.grid(row = 1, column = 1, columnspan = 1,
                             sticky = "nsew")
        self.confirmation_frame = ttk.Frame(self, borderwidth = 2,
                                            padding = 7)
        self.confirmation_frame.grid(row = 2, column = 1, columnspan = 1,
                                     sticky = "s")
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        # input frame contents        
        self.select_entry = ttk.Entry(self.input_frame)
        self.select_entry.pack(side = "left", expand = "true", fill = tk.BOTH,
                               padx = (0,5))
        self.select_button = ttk.Button(self.input_frame, text = "Search", 
                                       command = lambda: self.search_update())
        self.select_button.pack(side = "left")
        # results
        self.select_list = tk.Listbox(self.select_list_frame)
        self.select_list.pack(side = "left", expand = "true", fill = tk.BOTH)
        self.select_scroller = ttk.Scrollbar(self.select_list_frame,
                                             command = self.select_list.yview)
        self.select_scroller.pack(side = "right", fill = "y")
        self.select_list.config(yscrollcommand = self.select_scroller.set)
        # confirmation buttons
        self.ok_button = ttk.Button(self.confirmation_frame, text = "Select",
                                    padding = 3)
#        self.ok_button.configure(padx = 3, pady = 3)
        self.ok_button.pack(side = "right", padx = (2,0))
        self.cancel_button = ttk.Button(self.confirmation_frame,
                                        text = "Cancel",
                                        command = self.destroy)
        self.cancel_button.pack(side = "right", padx = (0,2))
        

    
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
        self.select_list.bind("<<ListboxSelect>>", self.select_list_update)
    
    def create_custom_widgets(self):
        self.label_name = ttk.Label(self.info_frame,
                                    text = "Airport Name : ")
        self.label_name.pack(anchor = "w")
        self.name_label = ttk.Label(self.info_frame, wraplength = 200)
        self.name_label.pack()
        self.label_icaocode = ttk.Label(self.info_frame,
                                        text = "ICAO Code : ")
        self.label_icaocode.pack(anchor = "w")
        self.icaocode_label = ttk.Label(self.info_frame)
        self.icaocode_label.pack()
        self.label_iatacode = ttk.Label(self.info_frame,
                                        text = "IATA Code : ")
        self.label_iatacode.pack(anchor = "w")
        self.iatacode_label = ttk.Label(self.info_frame)
        self.iatacode_label.pack()
                                        
    def select_list_update(self, event):
        selection = event.widget.curselection()
        index = selection[0]
        data = self.search_results[index]        
        self.name_label.configure(text = data[1])
        self.icaocode_label.configure(text = data[2])
        self.iatacode_label.configure(text = data[3])
