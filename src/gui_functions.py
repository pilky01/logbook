#!/usr/bin/env python3

import tkinter as tk


def create_database_window():

    cd_window = tk.Tk()
    cd_window.title('Create Database')
    cd_frame = CreateDatabaseWindow(cd_window)
    cd_frame.pack()
    
def record_window(source):#, datalist):
    record_window = tk.Tk()
    record_window.title(source)
    record_frame = RecordWindow(record_window)
    record_frame.pack()
