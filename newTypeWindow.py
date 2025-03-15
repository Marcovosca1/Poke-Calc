import customtkinter as ctk

class newTypeWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add a new type")
        self.mainFrame = ctk.CTkFrame(master=self)
        self.mainFrame.pack(padx=10, pady=10)
        self.loadFrame1()
        
    
    def loadFrame1(self):
        self.label = ctk.CTkLabel(master=self.mainFrame, text="(1/3)", font=("Arial", 12), text_color="#ffffff")
        self.label.pack(padx=5, pady=1)

        self.label = ctk.CTkLabel(master=self.mainFrame, text="Enter the name of the new type", font=("Arial", 14), text_color="#ffffff")
        self.label.pack(padx=5, pady=5)

        self.entry = ctk.CTkEntry(master=self.mainFrame, font=("Arial", 14), text_color="#ffffff")
        self.entry.pack()

        self.button = ctk.CTkButton(master=self.mainFrame, text="Add", fg_color="#ffffff", hover_color="#ffffff", font=("Arial", 14), text_color="#000000", border_color="#fdffbd", border_width=1, command=self.loadFrame2)
        self.button.pack(padx=5, pady=5)

    # def loadFrame2(self):
    #     # self.mainFrame.destroy()
    
    #     self.label = ctk.CTkLabel(master=self.mainFrame, text="(2/3)", font=("Arial", 12), text_color="#ffffff")
    #     self.label.pack(padx=5, pady=1)

    #     self.label = ctk.CTkLabel(master=self.mainFrame, text="Choose a color for the new type", font=("Arial", 14), text_color="#ffffff")
    #     self.label.pack(padx=5, pady=5)

    #     self.colorButton = ctk.CTkButton(master=self.mainFrame, text="Choose color", font=("Arial", 14), text_color="#000000", border_color="#fdffbd", border_width=1, command=self.loadFrame3)
    #     self.colorButton.pack(padx=5, pady=5)

    #     self.backBtn = ctk.CTkButton(master=self.mainFrame, text="Back", fg_color="#ffffff", hover_color="#ffffff", font=("Arial", 14), text_color="#000000", border_color="#fdffbd", border_width=1, command=self.loadFrame1)

    # def loadFrame3(self):
    #     # self.mainFrame.destroy()

    #     self.label = ctk.CTkLabel(master=self.mainFrame, text="(3/3)", font=("Arial", 12), text_color="#ffffff")
    #     self.label.pack(padx=5, pady=1)

    #     self.label = ctk.CTkLabel(master=self.mainFrame, text="Choose the weaknesses", font=("Arial", 14), text_color="#ffffff")
    
    # Add a list of buttons with the types
