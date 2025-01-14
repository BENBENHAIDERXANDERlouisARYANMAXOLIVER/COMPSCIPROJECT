import tkinter as tk

class DeleteFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>")

        # confirm deletion button
        loginbutton=tk.Button(self, text="Confirm Account deletion",command=self.DeleteAccount)
        loginbutton.grid(row=7,column=2,columnspan=2,sticky="NSWE")
        
        #stop deletion button button
        signupbutton=tk.Button(self, text="Signup",command=self.parent.switchtosettings)
        signupbutton.grid(row=7,column=3,columnspan=2,sticky="NSWE")
        
        

    

    def loadUp(self):
        print("loaded Login")
        # print("Bypassed login")
        # self.controller.successfulLogin("asmith")
    
   
        
    def DeleteAccount(self):
        print("WILL BE IMPLMENTED SOON TO PREVENT ERRORS AND ACCIDENTS")

    
        
        