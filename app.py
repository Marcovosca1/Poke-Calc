from typeButton import *

class App(ctk.CTk):
    def __init__(self, data):
        super().__init__()
        self.title("Pokemon Type Calculator")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

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
        for i in range(0, number):
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            btn = TypeButton(frame, data['Types'][i]['name'], data['Types'][i]['color'], adjust_brightness(data['Types'][i]['color'], 0.8))
            btn.grid(row=rowCount, column=colCount, padx=2, pady=2)
            colCount += 1
        if secondary:
            btn = ctk.CTkButton(master=frame, text="None", fg_color="#aaaaaa", hover_color=adjust_brightness("#aaaaaa", 0.8), text_color="#000000", border_color="#fdffbd", border_width=1)
            if number % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            btn.grid(row=rowCount, column=colCount, padx=2, pady=2)

# =========== DE ADAUGAT FUNCTIONALITATEA BUTOANELOR DIN TYPEBUTTON.PY =============
