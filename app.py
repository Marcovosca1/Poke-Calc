from typeButton import *

class App(ctk.CTk):
    def __init__(self, data):
        super().__init__()
        self.title("Pokemon Type Calculator")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Lists of buttons
        self.primaryList = []
        self.secondaryList = []

        # =========== FRAMES =============

        # Primary Type
        self.framePrimary = ctk.CTkFrame(master=self)
        self.framePrimary.grid(row=0, column=0, padx=5, pady=25, sticky="nsew")
        self.add_btns(self.framePrimary, data)

        # Secondary Type
        self.frameSecondary = ctk.CTkFrame(master=self)
        self.frameSecondary.grid(row=1, column=0, padx=5, pady=25, sticky="nsew")
        self.add_btns(self.frameSecondary, data, True)

        self.frameEmpty = ctk.CTkFrame(master=self)
        self.frameEmpty.grid(row=0, column=1, padx=20, pady=10, sticky="nsew", rowspan=2)

        # Weakness Display
        self.frameWeakness = ctk.CTkFrame(master=self)
        self.frameWeakness.grid(row=0, column=2, padx=5, pady=10, sticky="nsew", rowspan=2)
        
        self.Four = ctk.CTkLabel(master=self.frameWeakness, text="It takes 4x from:", font=("Arial", 14))
        self.Four.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")
        self.FourAns = ctk.CTkLabel(master=self.frameWeakness, text="", font=("Arial", 14))
        self.FourAns.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

        self.Two = ctk.CTkLabel(master=self.frameWeakness, text="It takes 2x from:", font=("Arial", 14))
        self.Two.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        self.TwoAns = ctk.CTkLabel(master=self.frameWeakness, text="", font=("Arial", 14))
        self.TwoAns.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")

        self.One = ctk.CTkLabel(master=self.frameWeakness, text="It takes 1x from:", font=("Arial", 14))
        self.One.grid(row=4, column=0, padx=20, pady=5, sticky="nsew")
        self.OneAns = ctk.CTkLabel(master=self.frameWeakness, text="", font=("Arial", 14))
        self.OneAns.grid(row=5, column=0, padx=20, pady=5, sticky="nsew")

        self.Half = ctk.CTkLabel(master=self.frameWeakness, text="It takes 0.5x from:", font=("Arial", 14))
        self.Half.grid(row=6, column=0, padx=20, pady=5, sticky="nsew")
        self.HalfAns = ctk.CTkLabel(master=self.frameWeakness, text="", font=("Arial", 14))
        self.HalfAns.grid(row=7, column=0, padx=20, pady=5, sticky="nsew")

        self.Quarter = ctk.CTkLabel(master=self.frameWeakness, text="It takes 0.25x from:", font=("Arial", 14))
        self.Quarter.grid(row=8, column=0, padx=20, pady=5, sticky="nsew")
        self.QuarterAns = ctk.CTkLabel(master=self.frameWeakness, text="", font=("Arial", 14))
        self.QuarterAns.grid(row=9, column=0, padx=20, pady=5, sticky="nsew")

        self.Zero = ctk.CTkLabel(master=self.frameWeakness, text="It takes 0x from:", font=("Arial", 14))
        self.Zero.grid(row=10, column=0, padx=20, pady=5, sticky="nsew")
        self.ZeroAns = ctk.CTkLabel(master=self.frameWeakness, text="", font=("Arial", 14))
        

        # =================================
        
        # Disabled buttons
        self.disabledPrimary = self.primaryList[0]
        self.primaryList[0].clicked()

        self.disabledSecondary = self.secondaryList[-1]
        self.secondaryList[-1].clicked()

        self.blockedSecondary = self.secondaryList[0]
        self.secondaryList[0].blocked()

    def add_btns(self, frame, data, secondary=False):
        number = data['Types'][-1]['id']
        rowCount = 0
        colCount = 0
        for i in range(0, number+1):
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            btn = TypeButton(frame, data['Types'][i]['name'], data['Types'][i]['color'], adjust_brightness(data['Types'][i]['color'], 0.8), i, self)
            btn.grid(row=rowCount, column=colCount, padx=2, pady=2)
            colCount += 1
            if secondary:
                self.secondaryList.append(btn)
            else:
                self.primaryList.append(btn)
        if secondary:
            btn = TypeButton(frame, "None", "#aaaaaa", adjust_brightness("#aaaaaa", 0.8), number+1, self)
            self.secondaryList.append(btn)
            if (number+1) % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            btn.grid(row=rowCount, column=colCount, padx=2, pady=2)

    def btn_click(self, frame, index):
        if frame == self.framePrimary:
            self.primaryList[self.disabledPrimary.index].normal()
            self.secondaryList[self.blockedSecondary.index].normal()
            
            self.disabledPrimary = self.primaryList[index]
            self.primaryList[index].clicked()
            
            self.blockedSecondary = self.secondaryList[index]
            self.secondaryList[index].blocked()
        elif frame == self.frameSecondary:
            self.secondaryList[self.disabledSecondary.index].normal()
            
            self.disabledSecondary = self.secondaryList[index]
            self.secondaryList[index].clicked()
        

# =========== DE ADAUGAT FUNCTIONALITATEA BUTOANELOR DIN TYPEBUTTON.PY =============
