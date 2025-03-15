from app import *
import json

if __name__ == "__main__":
    f = open("Datas/types1.json")
    data = json.load(f)

    mainApp = App(data)
    mainApp.mainloop()