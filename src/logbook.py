#!/usr/bin/env python3

import tkinter as tk

import logbook_gui as gui

def main():
    root = tk.Tk()
    gui.Application(root).pack()

    root.title('Logbook')
    root.geometry("800x300")
    root.mainloop()

if __name__ == "__main__":
    main()
