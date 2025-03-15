from customtkinter import *
import newTypeWindow as ntw

import tkinter as tk

class FileMenu(tk.Menu):
    def __init__(self, master, tearoff=0):
        super().__init__(master, tearoff=tearoff)
        self.add_command(label="Add a new type", command=self.newTypeFunc)
        self.add_command(label="Delete am existing type", command=self.newDeleteFunc)
        self.add_command(label="Revert to default", command=self.newRevertFunc)
        self.add_command(label="Save")
        self.add_command(label="Exit")

        self.toplevel_window = None

    def newRevertFunc(self):
        print("New function called")

    def newTypeFunc(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ntw.newTypeWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def newDeleteFunc(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ntw.newTypeWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it