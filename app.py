from typeButton import *


class App(ctk.CTk):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.title("Pokemon Type Calculator")
        self.root = ctk.CTkFrame(master=self)
        self.root.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Lists of buttons
        self.primaryList = []
        self.secondaryList = []

        self.fourList = []
        self.twoList = []
        self.oneList = []
        self.halfList = []
        self.quarterList = []
        self.zeroList = []

        # =========== FRAMES =============

        # Primary Type
        self.framePrimary = ctk.CTkFrame(master=self.root)
        self.framePrimary.grid(row=0, column=0, padx=5, pady=25, sticky="nsew")
        self.add_btns(self.framePrimary, data)

        # Secondary Type
        self.frameSecondary = ctk.CTkFrame(master=self.root)
        self.frameSecondary.grid(row=1, column=0, padx=5, pady=25, sticky="nsew")
        self.add_btns(self.frameSecondary, data, True)

        # Weakness Display
        self.frameWeakness = ctk.CTkFrame(master=self.root)
        self.frameWeakness.grid(row=0, column=2, padx=5, pady=10, sticky="nsew", rowspan=2)

        self.Four = ctk.CTkLabel(master=self.frameWeakness, text="It takes 4x from:", font=("Arial", 14))
        self.Four.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")
        self.FourAns = ctk.CTkFrame(master=self.frameWeakness, height=50)
        self.FourAns.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.Two = ctk.CTkLabel(master=self.frameWeakness, text="It takes 2x from:", font=("Arial", 14))
        self.Two.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        self.TwoAns = ctk.CTkFrame(master=self.frameWeakness, height=50)
        self.TwoAns.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        self.One = ctk.CTkLabel(master=self.frameWeakness, text="It takes 1x from:", font=("Arial", 14))
        self.One.grid(row=4, column=0, padx=20, pady=5, sticky="nsew")
        self.OneAns = ctk.CTkFrame(master=self.frameWeakness, height=50)
        self.OneAns.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        self.Half = ctk.CTkLabel(master=self.frameWeakness, text="It takes 0.5x from:", font=("Arial", 14))
        self.Half.grid(row=6, column=0, padx=20, pady=5, sticky="nsew")
        self.HalfAns = ctk.CTkFrame(master=self.frameWeakness, height=50)
        self.HalfAns.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

        self.Quarter = ctk.CTkLabel(master=self.frameWeakness, text="It takes 0.25x from:", font=("Arial", 14))
        self.Quarter.grid(row=8, column=0, padx=20, pady=5, sticky="nsew")
        self.QuarterAns = ctk.CTkFrame(master=self.frameWeakness, height=50)
        self.QuarterAns.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

        self.Zero = ctk.CTkLabel(master=self.frameWeakness, text="It takes 0x from:", font=("Arial", 14))
        self.Zero.grid(row=10, column=0, padx=20, pady=5, sticky="nsew")
        self.ZeroAns = ctk.CTkFrame(master=self.frameWeakness, height=50)
        self.ZeroAns.grid(row=11, column=0, padx=5, pady=5, sticky="nsew")
        

        # =================================
        
        # Disabled buttons
        self.disabledPrimary = self.primaryList[0]
        self.primaryList[0].clicked()

        self.disabledSecondary = self.secondaryList[-1]
        self.secondaryList[-1].clicked()

        self.blockedSecondary = self.secondaryList[0]
        self.secondaryList[0].blocked()

        # ==================================

        self.calculate(data)

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
            
            # If the primary type is the same as the secondary type, put the secondary type to None
            if self.disabledPrimary.index == self.disabledSecondary.index:
                self.secondaryList[self.disabledSecondary.index].normal()
                self.disabledSecondary = self.secondaryList[-1]
                self.secondaryList[-1].clicked()

            self.blockedSecondary = self.secondaryList[index]
            self.secondaryList[index].blocked()


        elif frame == self.frameSecondary:
            self.secondaryList[self.disabledSecondary.index].normal()
            
            self.disabledSecondary = self.secondaryList[index]
            self.secondaryList[index].clicked()

        self.calculate(self.data)

    def calculate(self, data):
        self.clean()
        result = None

        for i in range(0, len(self.primaryList)):
            if self.disabledSecondary.index == self.secondaryList[-1].index:
                result = data['Types'][i]['weakness'][self.disabledPrimary.index]
            else:
                result = data['Types'][i]['weakness'][self.disabledPrimary.index] * data['Types'][i]['weakness'][self.disabledSecondary.index]
            match result:
                case 4:
                    self.fourList.append(self.primaryList[i])
                    print(f"{self.primaryList[i]._text} is 4 times")
                case 2:
                    self.twoList.append(self.primaryList[i])
                    print(f"{self.primaryList[i]._text} is 2 times")
                case 1:
                    self.oneList.append(self.primaryList[i])
                    print(f"{self.primaryList[i]._text} is 1 time")
                case 0.5:
                    self.halfList.append(self.primaryList[i])
                    print(f"{self.primaryList[i]._text} is 0.5 times")
                case 0.25:
                    self.quarterList.append(self.primaryList[i])
                    print(f"{self.primaryList[i]._text} is 0.25 times")
                case 0:
                    self.zeroList.append(self.primaryList[i])
                    print(f"{self.primaryList[i]._text} is 0 times")
        print("=====================================")
        self.showResults(data)


    def showResults(self, data):
        rowCount = 0
        colCount = 0
        for i in range(0, len(self.fourList)):
            typeLabel = ctk.CTkLabel(master=self.FourAns, text=self.fourList[i]._text, fg_color=self.fourList[i].mainColor, text_color="white", width=100)
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            typeLabel.grid(row=rowCount, column=colCount, padx=2, pady=2)

        rowCount = 0
        colCount = 0
        for i in range(0, len(self.twoList)):
            typeLabel = ctk.CTkLabel(master=self.TwoAns, text=self.twoList[i]._text, fg_color=self.twoList[i].mainColor, text_color="white", width=100)
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            typeLabel.grid(row=rowCount, column=colCount, padx=2, pady=2)

        rowCount = 0
        colCount = 0
        for i in range(0, len(self.oneList)):
            typeLabel = ctk.CTkLabel(master=self.OneAns, text=self.oneList[i]._text, fg_color=self.oneList[i].mainColor, text_color="white", width=100)
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            typeLabel.grid(row=rowCount, column=colCount, padx=2, pady=2)

        rowCount = 0
        colCount = 0
        for i in range(0, len(self.halfList)):
            typeLabel = ctk.CTkLabel(master=self.HalfAns, text=self.halfList[i]._text, fg_color=self.halfList[i].mainColor, text_color="white", width=100)
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            typeLabel.grid(row=rowCount, column=colCount, padx=2, pady=2)

        rowCount = 0
        colCount = 0
        for i in range(0, len(self.quarterList)):
            typeLabel = ctk.CTkLabel(master=self.QuarterAns, text=self.quarterList[i]._text, fg_color=self.quarterList[i].mainColor, text_color="white", width=100)
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            typeLabel.grid(row=rowCount, column=colCount, padx=2, pady=2)

        rowCount = 0
        colCount = 0
        for i in range(0, len(self.zeroList)):
            typeLabel = ctk.CTkLabel(master=self.ZeroAns, text=self.zeroList[i]._text, fg_color=self.zeroList[i].mainColor, text_color="white", width=100)
            if i % 3 == 0:
                rowCount += 1
                colCount = 0
            else:
                colCount += 1
            typeLabel.grid(row=rowCount, column=colCount, padx=2, pady=2)

    def clean(self):
        self.fourList.clear()
        self.twoList.clear()
        self.oneList.clear()
        self.halfList.clear()
        self.quarterList.clear()
        self.zeroList.clear()

        for widget in self.FourAns.winfo_children():
            widget.destroy()
        for widget in self.TwoAns.winfo_children():
            widget.destroy()
        for widget in self.OneAns.winfo_children():
            widget.destroy()
        for widget in self.HalfAns.winfo_children():
            widget.destroy()
        for widget in self.QuarterAns.winfo_children():
            widget.destroy()
        for widget in self.ZeroAns.winfo_children():
            widget.destroy()