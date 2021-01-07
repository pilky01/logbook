#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkcal
import tkinter.messagebox

import logbook_db as db
from gui_components import TimePicker as TimePicker


class Application(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #self.config(width = 680)
        self.create_application()
    
    def create_application(self):
        self.taskbar = Taskbar(self)
        self.taskbar.grid(row = 0, column = 0)


class Taskbar(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_buttons()

    def create_buttons(self):
        # Views
        self.view_frame = ttk.Frame(self)
        self.view_frame.grid(row = 0, column = 0)
        self.view_dashboard = ttk.Button(self.view_frame,
                                         text = "Dashboard View")
        self.view_dashboard.grid(row = 0, column = 0)
        self.view_flightlist = ttk.Button(self.view_frame,
                                          text = "Flight List View")
        self.view_flightlist.grid(row = 0, column = 1)
        self.view_calendar = ttk.Button(self.view_frame,
                                        text = "Calendar View")
        self.view_calendar.grid(row = 0, column = 2)
        # Functions
        self.function_frame = ttk.Frame(self)
        self.function_frame.grid(row = 0, column = 1)
        self.function_newrecord = ttk.Button(self.function_frame,
                                             text = "New Record",
                                   command = lambda: self.new_flight_record())
        self.function_newrecord.grid(row = 0, column = 0)
        self.function_newaircraft = ttk.Button(self.function_frame,
                                             text = "New Aircraft",
                                        command = lambda: self.new_aircraft())
        self.function_newaircraft.grid(row = 0, column = 1)
        self.function_newairfield = ttk.Button(self.function_frame,
                                             text = "New Airfield")#,
                                  #command = lambda: self.new_flight_record())
        self.function_newairfield.grid(row = 0, column = 2)
        self.function_newcrew = ttk.Button(self.function_frame,
                                             text = "New Crewmember")#,
                                  #command = lambda: self.new_flight_record())
        self.function_newcrew.grid(row = 0, column = 3)
        
    def new_flight_record(self):
        self.record_window = FlightRecordWindow(self,
                                      record_data = [None for i in range(26)])
        self.record_window.title("New Flight")
    
    def new_aircraft(self):
        self.aircraft_window = AircraftRecordWindow(self,
                                      record_data = [None for i in range (7)])
        self.aircraft_window.title("New Aircraft")


class Dashboard(ttk.Frame):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
class BaseRecordWindow(tk.Toplevel):
    
    def __init__(self, master = None, record_data = [], *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.record_data = record_data


class FlightRecordWindow(BaseRecordWindow):
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.create_record_widgets()
        
    def create_record_widgets(self):
        # Airfield Frame
        self.airfield_data_frame = ttk.Labelframe(self,
                                                  text = "Airfield Data")
        self.airfield_data_frame.grid(row = 0, column = 0, sticky = "nsew")
        ## Origin
        self.origin_label = ttk.Label(self.airfield_data_frame,
                                      text = "Origin Airport", anchor = "w")
        self.origin_label.grid(row = 0, column = 0, sticky = "ew")
        self.origin_var = tk.StringVar(self)
        self.origin_entry = ttk.Entry(self.airfield_data_frame,
                                      state = "readonly",
                                      textvariable = self.origin_var)
        self.origin_entry.grid(row = 1, column = 0)
        self.origin_select = ttk.Button(self.airfield_data_frame, 
                                        text = "...", width = 2,
                                        padding = 0,
                         command = lambda: self.create_origin_select_window())
        self.origin_select.grid(row = 1, column = 1)
        ## Destination
        self.destination_label = ttk.Label(self.airfield_data_frame,
                                           text = "Destination Airport",
                                           anchor = "w")
        self.destination_label.grid(row = 2, column = 0, sticky = "ew")
        self.destination_var = tk.StringVar(self)
        self.destination_entry = ttk.Entry(self.airfield_data_frame,
                                          state = "readonly",
                                          textvariable = self.destination_var)
        self.destination_entry.grid(row = 3, column = 0)
        self.destination_select = ttk.Button(self.airfield_data_frame, 
                                             text = "...", width = 2,
                                             padding = 0,
                    command = lambda: self.create_destination_select_window())
        self.destination_select.grid(row = 3, column = 1)
        # Times Frame
        self.times_frame = ttk.Labelframe(self, text = "Times")
        self.times_frame.grid(row = 0, column = 1, rowspan = 2,
                              sticky = "nsew")
        ## Departure
        self.depart_date_label = ttk.Label(self.times_frame, anchor = "w",
                                           text = "Departure Date")
        self.depart_date_label.grid(row = 0, column = 0, sticky = "ew")
        self.depart_date_entry = tkcal.DateEntry(self.times_frame)
        self.depart_date_entry.grid(row = 1, column = 0)
        self.depart_time_label = ttk.Label(self.times_frame,
                                           text = "Time (z)", anchor = "w")
        self.depart_time_label.grid(row = 0, column = 1, sticky = "ew")
        self.depart_time_picker = TimePicker(self.times_frame)
        self.depart_time_picker.grid(row = 1, column = 1, sticky = "ew")
        ## Arrival
        self.arrival_date_label = ttk.Label(self.times_frame, anchor = "w",
                                            text = "Arrival Date")
        self.arrival_date_label.grid(row = 2, column = 0, sticky = "ew")
        self.arrival_date_entry = tkcal.DateEntry(self.times_frame)
        self.arrival_date_entry.grid(row = 3, column = 0)
        self.arrival_time_label = ttk.Label(self.times_frame, 
                                            text = "Time (z)", anchor = "w")
        self.arrival_time_label.grid(row = 2, column = 1, sticky = "ew")
        self.arrival_time_picker = TimePicker(self.times_frame)
        self.arrival_time_picker.grid(row = 3, column = 1, sticky = "ew")
        self.total_time_label = ttk.Label(self.times_frame,
                                          text = "Total Time:", anchor = "e")
        self.total_time_label.grid(row = 4, column = 0, sticky = "ew")
        self.total_time_var = tk.StringVar(self.times_frame)
        #self.total_time_var.set()
        self.total_time_entry = ttk.Entry(self.times_frame, width = 10,
                                          state = "readonly",
                                          textvariable = self.total_time_var)
        self.total_time_entry.grid(row = 4, column = 1)
        ## Operating Capacity
        self.operating_capacity_var = tk.StringVar()
        self.operating_capacity_label = ttk.Label(self.times_frame,
                                                  anchor = "w",
                                                  text = "Operating Capacity")
        self.operating_capacity_label.grid(row = 0, column = 3, sticky = "ew",
                                           columnspan = 2)
        self.p1_radiobutton = ttk.Radiobutton(self.times_frame,
                                       value = "p1", text = "P1",
                                       variable = self.operating_capacity_var)
        self.p1_radiobutton.grid(row = 1, column = 3, sticky = "ew")
        self.picus_radiobutton = ttk.Radiobutton(self.times_frame,
                                       value = "picus", text = "PICUS",
                                       variable = self.operating_capacity_var)
        self.picus_radiobutton.grid(row = 1, column = 4, sticky = "ew")
        self.p2_radiobutton = ttk.Radiobutton(self.times_frame,
                                       value = "p2", text = "P2",
                                       variable = self.operating_capacity_var)
        self.p2_radiobutton.grid(row = 3, column = 3, sticky = "ew")
        self.dual_radiobutton = ttk.Radiobutton(self.times_frame,
                                       value = "dual", text = "Dual",
                                       variable = self.operating_capacity_var)
        self.dual_radiobutton.grid(row = 3, column = 4, sticky = "ew")
        self.op_cap_button = ttk.Button(self.times_frame, text = "Print Var",
                   command = lambda: print(self.operating_capacity_var.get()))
        self.op_cap_button.grid(row = 4, column = 4)
        # Aircraft Frame
        self.aircraft_data_frame = ttk.Labelframe(self, text = "Aircraft")
        self.aircraft_data_frame.grid(row = 1, column = 0, sticky = "nsew")
        self.aircraft_registration_label = ttk.Label(self.aircraft_data_frame,
                                                     text = "Registration:")
        self.aircraft_registration_label.grid(row = 1, column = 0,
                                              sticky = "ew")
        self.aircraft_registration = ttk.Label(self.aircraft_data_frame)
        self.aircraft_registration.grid(row = 2, column = 0)
        self.aircraft_type_label = ttk.Label(self.aircraft_data_frame,
                                             text = "Type:")
        self.aircraft_type_label.grid(row = 3, column = 0, sticky = "ew")
        self.aircraft_type = ttk.Label(self.aircraft_data_frame)
        self.aircraft_type.grid(row = 4, column = 0)
        self.aircraft_multi_label = ttk.Label(self.aircraft_data_frame,
                                              text = "Multi-engine")
        self.aircraft_multi_label.grid(row = 5, column = 0)
        self.aircraft_multi_label_check =\
                                     tk.Checkbutton(self.aircraft_data_frame)
        self.aircraft_multi_label_check.grid(row = 5, column = 1,
                                             sticky = "e")
        self.aircraft_select_button = ttk.Button(self.aircraft_data_frame,
                                                text = "Select...",
                       command = lambda: self.create_aircraft_select_window())
        self.aircraft_select_button.grid(row = 0, column = 0)
        # Comments Frame
        ##Max length validation
        self.comments_frame = ttk.Labelframe(self, text = "Comments")
        self.comments_frame.grid(row = 2, column = 1, rowspan = 2)
        self.comments_text = tk.Text(self.comments_frame, wrap = "none",
                                      height = 5, width = 24)
        self.comments_text.grid(row = 0, column = 0)
        self.comments_xscroller = ttk.Scrollbar(self.comments_frame,
                                                orient = "horizontal",
                                           command = self.comments_text.xview)
        self.comments_xscroller.grid(row = 1, column = 0, sticky = "ew")
        self.comments_yscroller = ttk.Scrollbar(self.comments_frame,
                                                orient = "vertical",
                                           command = self.comments_text.yview)
        self.comments_yscroller.grid(row = 0, column = 1, sticky = "ns")
        self.comments_text.config(yscrollcommand =\
                                                  self.comments_yscroller.set,
                                  xscrollcommand =\
                                                  self.comments_xscroller.set)
        # Crew Frame
        self.crew_frame = ttk.Labelframe(self, text = "Crew")
        self.crew_frame.grid(row = 2, column = 0, rowspan = 3,
                             sticky = "nsew")
        self.crew_add_button = ttk.Button(self.crew_frame, text = "Add...")
        self.crew_add_button.grid(row = 0, column = 0)
        # Confirmation Buttons
        self.confirmation_frame = ttk.Frame(self, borderwidth = 2,
                                            padding = 7)
        self.confirmation_frame.grid(row = 4, column = 1, sticky = "s")
        self.cancel_button = ttk.Button(self.confirmation_frame, 
                                        text = "Cancel",
            #create method to check for non-empty form, "do you want to save?"
                                        command = self.destroy)
        self.cancel_button.grid(row = 0, column = 0)
        self.save_button = ttk.Button(self.confirmation_frame, text = "Save",
                                    command = lambda: print(self.record_data))
        self.save_button.grid(row = 0, column = 1)
        
    def create_origin_select_window(self):
        self.origin_select_window = AirfieldSelectWindow(self,
                                            source = "origin", listindex = 1,
                                            return_variable = self.origin_var)
        self.origin_select_window.title("Select Origin...")
        #origin_select_window.geometry("500x350")
    
    def create_destination_select_window(self):
        self.destination_select_window = AirfieldSelectWindow(self,
                                       source = "destination", listindex = 2,
                                       return_variable = self.destination_var)
        self.destination_select_window.title("Select Destination...")
    
    def create_aircraft_select_window(self):
        self.aircraft_select_window = AircraftSelectWindow(self,)
        self.aircraft_select_window.title("Select Aircraft...")


class AircraftRecordWindow(BaseRecordWindow):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.create_widgets()
        
    def create_widgets(self):
        self.button = ttk.Button(self, text = "test",
                                 command = lambda: self.record_test())
        self.button.grid(row = 0, column = 0)
    
    def record_test(self):
        print(self.record_data)

class BaseSelectWindow(tk.Toplevel):
    
    def __init__(self, master = None, source = None, return_variable = None,
                 listindex = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(padx = 10, pady = 10)
        self.master = master
        self.source = source
        self.return_variable = return_variable
        self.listindex = listindex
        self.search_results = []
        self.create_base_widgets()
    
    def create_base_widgets(self):
        #frames
        self.input_frame = ttk.Frame(self, padding = 2)
        self.input_frame.grid(row = 0, column = 0, columnspan = 2,
                              sticky = "nsew")
        self.select_list_frame = ttk.Frame(self, padding = 2)
        self.select_list_frame.grid(row = 1, column = 0, rowspan = 2,
                                    sticky = "nsew")
        self.info_frame = ttk.Frame(self, borderwidth = 2, padding = 2)
        self.info_frame.grid(row = 1, column = 1, sticky = "nsew")
        self.confirmation_frame = ttk.Frame(self, borderwidth = 2,
                                            padding = 7)
        self.confirmation_frame.grid(row = 2, column = 1, sticky = "s")
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        # input frame contents        
        self.select_entry = ttk.Entry(self.input_frame)
        self.select_entry.pack(side = "left", expand = "true", fill = tk.BOTH,
                               padx = (0,10))
        self.select_button = ttk.Button(self.input_frame, text = "Search", 
                                       command = lambda: self.search_update())
        self.select_button.pack(side = "left")
        # results
        self.select_list = tk.Listbox(self.select_list_frame, width = 28)
        self.select_list.pack(side = "left", expand = "true", fill = tk.BOTH)
        self.select_scroller = ttk.Scrollbar(self.select_list_frame,
                                             command = self.select_list.yview)
        self.select_scroller.pack(side = "right", fill = "y")
        self.select_list.config(yscrollcommand = self.select_scroller.set)
        # confirmation buttons
        self.ok_button = ttk.Button(self.confirmation_frame, text = "Select",
                                   padding = 3,
                                   command = lambda: self.confirm_selection())
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
    
    def confirm_selection(self):
        if self.select_list.curselection():
            int_select = self.select_list.curselection()
            selection_string = self.select_list.get(int_select)
            self.return_variable.set(selection_string)
            # insert selection id into list position
            self.master.record_data[self.listindex] =\
                                         self.search_results[int_select[0]][0]
            self.destroy()
        else:
            tk.messagebox.showerror("Error",
              "Nothing selected.\nPlease make a selection before continuing.",
                                    parent = self)


class AirfieldSelectWindow(BaseSelectWindow):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.create_custom_widgets()
        self.select_list.bind("<<ListboxSelect>>", self.select_list_update)
    
    def create_custom_widgets(self):
        self.label_name = ttk.Label(self.info_frame,
                                    text = "Airport Name: ")
        self.label_name.pack(anchor = "w")
        self.name_label = tk.Label(self.info_frame, wraplength = 200,
                                    justify = "center", width = 32,
                                    height = 3 , anchor = "center")
        self.name_label.pack()
        self.label_icaocode = ttk.Label(self.info_frame,
                                        text = "ICAO Code: ")
        self.label_icaocode.pack(anchor = "w")
        self.icaocode_label = tk.Label(self.info_frame, justify = "center",
                                       anchor = "center", height = 2)
        self.icaocode_label.pack()
        self.label_iatacode = ttk.Label(self.info_frame,
                                        text = "IATA Code: ")
        self.label_iatacode.pack(anchor = "w")
        self.iatacode_label = tk.Label(self.info_frame, justify = "center",
                                       anchor = "center", height = 2)
        self.iatacode_label.pack()
                                        
    def select_list_update(self, event):
        selection = event.widget.curselection()
        if len(selection) == 0:
            pass
        else:
            index = selection[0]
            data = self.search_results[index]        
            self.name_label.configure(text = data[1])
            self.icaocode_label.configure(text = data[2])
            self.iatacode_label.configure(text = data[3])


class AircraftSelectWindow(BaseSelectWindow):

    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        
