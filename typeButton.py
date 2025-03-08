import customtkinter as ctk
from globals import * 

class TypeButton(ctk.CTkButton):
    def __init__(self, master, text, fg_color, hover_color, font=("Arial", 14), text_color="#000000", border_color="#fdffbd", border_width = 1):
        super().__init__(master=master, text=text, fg_color=fg_color, hover_color=hover_color, font=font, text_color=text_color, border_color=border_color, border_width=border_width, command=self.clicked)

    def clicked(self):
        self.configure(state="disabled")
        self.configure(fg_color=adjust_brightness(self.cget("fg_color"), 0.5))
        # if  self.master == frameSecondary:
        #     disabledSecondary = self.cget("text")
        #     print(disabledSecondary)
        # else:
        #     disabledPrimary = self.cget("text")
        #     blockedSecondary = self.blocked()
        #     print(disabledPrimary)

    def blocked(self):
        self.configure(state="disabled")
        self.configure(fg_color=adjust_brightness(self.cget("fg_color"), 1.2))