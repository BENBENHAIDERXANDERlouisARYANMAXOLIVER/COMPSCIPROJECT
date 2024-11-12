import tkinter as tk

class ReviewFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>")


      

        
        

       
    

      

   

    def loadUp(self):
        print("loaded Login")
        #usernamebox text
        
        if (self.parent.AnswerCorrect==False):
            self.textcolor="Red"
            self.textcontents="Incorrect"
        elif(self.parent.AnswerCorrect==True):
            self.textcolor="Green"
            self.textcontents="Correct"
            
        
        #question C/W label
        self.right_or_wrong = tk.Label(self, text=self.textcontents,fg=self.textcolor)
        self.right_or_wrong.grid(row=8, column=1, sticky="NSWE")
        self.right_or_wrong.configure(background="white")
        self.right_or_wrong.config(font=("Georgia", 24))
    

        #error label
        self.errorlabel = tk.Label(self, text="", font=("Georgia", 54))
        self.errorlabel.configure(background="white")

        
       


       # blank filler rows
        self.rowconfigure(2,minsize=200)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(6, weight=1)   

        self.rowconfigure(4,minsize=50)
        self.rowconfigure(6,minsize=50)
        # print("Bypassed login")
        # self.controller.successfulLogin("asmith")
    
    def NewUserSignup(self):
       
        c = self.parent.db.cursor()
        
        r = c.execute("SELECT * FROM  tbluserdetails WHERE firstname=?" ,[self.usernamebox.get()])
        rfound=c.fetchall()
        if len(rfound) >0:
            print("Error")
            return False
        else:

       # c = self.parent.db.cursor()
            r = c.execute("INSERT INTO  tbluserdetails (firstname,surname,password) VALUES (?,?,?)" ,[self.usernamebox.get(),self.usernamebox.get(),self.passwordbox.get()])
            self.parent.db.commit()
            print("Success")
            self.errorlabel.grid(row=1, column=2, columnspan=2, sticky="NSEW")
         
            self.errorlabel.config(text="NEW ACCOUNT CREATED")
    def loginSubmitted(self):
                         
        c = self.parent.db.cursor()
        r = c.execute("SELECT * FROM tbluserdetails WHERE firstname = ? and password = ?", [self.usernamebox.get(), self.passwordbox.get()])
        results = r.fetchall()
        self.errorlabel.grid(row=1, column=2, columnspan=2, sticky="NSEW")
        
        if len(results)>0:
        #if True:
            self.errorlabel.config(text="Successful login")
            self.parent.successfulLogin(self.usernamebox.get())
            print("success)")
            return True
        else:
           self.errorlabel.config(text="Failure to login")
           print("Failure")
           return False
        
