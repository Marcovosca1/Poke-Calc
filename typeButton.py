import customtkinter as ctk
from globals import *
import json

class TypeButton(ctk.CTkButton):
    def __init__(self, master, text, fg_color, hover_color, index, context,font=("Arial", 14), text_color="#000000", border_color="#fdffbd", border_width = 1):
        super().__init__(master=master, text=text, fg_color=fg_color, hover_color=hover_color, font=font, text_color=text_color, border_color=border_color, border_width=border_width, command=self.onClick)
        self.index = index
        self.context = context
        self.mainColor = fg_color

    def onClick(self):
        self.context.btn_click(self.master, self.index)

    def returnIndex(self):
        return self.index

    def normal(self):
        self.configure(state="normal")
        self.configure(fg_color=self.mainColor)

    def clicked(self):
        self.configure(state="disabled")
        self.configure(fg_color=adjust_brightness(self.cget("fg_color"), 0.5))

    def blocked(self):
        self.configure(state="disabled")
        self.configure(fg_color=adjust_brightness(self.cget("fg_color"), 1.2))