#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkcal

import logbook_gui as gui


def main():
    root = tk.Tk()
    root.title('Logbook')
    root.geometry("600x300")

    taskbar = gui.Taskbar(root)
    taskbar.pack()

    app = gui.Application(root)
    app.mainloop()

if __name__ == "__main__":
    main()
