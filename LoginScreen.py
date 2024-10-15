import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>", self.keypressed)


        
        self.TitleLabel = tk.Canvas(self, width=500, height=138, bg="white", borderwidth=0, highlightthickness=0)
        self.Physicslogo= tk.PhotoImage(file="physicstesterlogo.png")
        self.TitleLabel.create_image(0,0 ,image=self.Physicslogo, anchor="nw")
        self.TitleLabel.configure(background="white")
        

        self.TitleLabel.grid(row=0, column=2, columnspan=2, sticky="NSWE")


        self.errorlabel = tk.Label(self, text="", font=("Georgia", 54))
        self.errorlabel.configure(background="white")
       
       
        self.rowconfigure(2,minsize=200)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(6, weight=1)   

        self.rowconfigure(4,minsize=50)
        self.rowconfigure(6,minsize=50)

        
        self.usernamebox = tk.Entry(self,text="Enter Username")
        self.usernamebox.grid(row=3,column=2,columnspan=2,sticky="NSEW")
        

        
        self.passwordbox = tk.Entry(self,text="Enter Password")
        self.passwordbox.grid(row=5,column=2,columnspan=2,sticky="NSEW")
        

        unamelabel = tk.Label(self, text="Username")
        unamelabel.grid(row=3, column=1, columnspan=1, sticky="NSWE")
        unamelabel.configure(background="white")
        unamelabel.config(font=("Arial", 24))
    
        pwordlabel = tk.Label(self, text="Password")
        pwordlabel.grid(row=5, column=1, columnspan=1, sticky="NSWE")
        pwordlabel.configure(background="white")
        pwordlabel.config(font=("Arial", 24))
        
        loginbutton=tk.Button(self, text="Login",command=loginSubmitted)
        loginbutton.grid(row=7,column=2,columnspan=1,sticky="NSWE")
        
        
        signupbutton=tk.Button(self, text="Signup")
        signupbutton.grid(row=7,column=3,columnspan=1,sticky="NSWE")

    def keypressed(self,event):
        # they pressed return. have they entered a username yet?
        if len(self.usernamebox.get())>0:
            self.loginSubmitted()

    def loadUp(self):
        print("loaded Login")
        # print("Bypassed login")
        # self.controller.successfulLogin("asmith")
    def NewUserSignup(self):
        c=self.parent.db.cursor()
        c.execute("INSERT INTO  tbluserdetails (firstname,secondname,password) VALUES ?,?,?" ,[self.usernamebox.get(),self.usernamebox.get(),self.passwordbox.get()])
        
        
    
    def loginSubmitted(self,loginbutton):
                         
        c = self.parent.db.cursor()
        r = c.execute("SELECT * from tbluserdetails WHERE firstname = ? and password = ?", [self.usernamebox.get(), self.passwordbox.get()])
        results = r.fetchall()
        self.errorlabel.grid(row=1, column=2, columnspan=2, sticky="NSEW")
        
        if len(results)>0:
        #if True:
            self.errorlabel.config(text="")
            self.parent.successfulLogin(self.usernamebox.get())
            print("success)")
            return True
        else:
           self.errorlabel.config(text="Failure to login")
           print("Failure")
           return False
        
