import tkinter as tk

class dataFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        

    def loadUp(self):
        print("L")
        c = self.parent.db.cursor()
        
        r = c.execute("SELECT * FROM  tblquestions")
        rfound=r.fetchall()
        print(rfound)


