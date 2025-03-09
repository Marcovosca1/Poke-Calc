from typeButton import *

class App(ctk.CTk):
    def __init__(self, data):
        super().__init__()
        self.title("Pokemon Type Calculator")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Disabled buttons
        self.disabledPrimary = None
        self.disabledSecondary = None
        self.blockedSecondary = None

        # Lists of buttons
        self.primaryList = []
        self.secondaryList = []

        # Primary Type
        self.framePrimary = ctk.CTkFrame(master=self)
        self.framePrimary.grid(row=0, column=0, padx=5, pady=20, sticky="nsew")
        self.add_btns(self.framePrimary, data)

        # Secondary Type
        self.frameSecondary = ctk.CTkFrame(master=self)
        self.frameSecondary.grid(row=1, column=0, padx=5, pady=20, sticky="nsew")
        self.add_btns(self.frameSecondary, data, True)

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
            if (number+1) % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            btn.grid(row=rowCount, column=colCount, padx=2, pady=2)

    def btn_click(self, frame, index):
        if frame == self.framePrimary:
            print(f"{self.primaryList[index]._text} has been clicked")
        # elif frame == self.frameSecondary and self.disabledSecondary != :
        

# =========== DE ADAUGAT FUNCTIONALITATEA BUTOANELOR DIN TYPEBUTTON.PY =============
