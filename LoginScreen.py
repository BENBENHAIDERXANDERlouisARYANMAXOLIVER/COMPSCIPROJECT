import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)

        self.parent.bind("<Return>", self.keypressed)
        TitleLabel = tk.Label(self, text="Welcome to PhysicsTester")
        TitleLabel.grid(row=0, column=2, columnspan=2, sticky="NSWE")
        TitleLabel.config(font=("Arial", 24))

        self.errorLabel = tk.Label(self, text="", font=("Arial", 24))
        self.errorLabel.grid(row=1, column=2, columnspan=2, sticky="NSEW")
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(6, weight=1)   

        self.rowconfigure(2,minsize=200)
        self.rowconfigure(4,minsize=50)
        self.rowconfigure(6,minsize=50)
        
        usernamebox = tk.Entry(self,text="Enter Username")
        usernamebox.grid(row=3,column=2,columnspan=2,sticky="NSEW")
        

        
        passwordbox = tk.Entry(self,text="Enter Password")
        passwordbox.grid(row=5,column=2,columnspan=2,sticky="NSEW")
        

        unamelabel = tk.Label(self, text="Username")
        unamelabel.grid(row=3, column=1, columnspan=1, sticky="NSWE")
        unamelabel.config(font=("Arial", 24))
    
        pwordlabel = tk.Label(self, text="Password")
        pwordlabel.grid(row=5, column=1, columnspan=1, sticky="NSWE")
        pwordlabel.config(font=("Arial", 24))
        
        loginbutton=tk.Button(self, text="Login")
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

    def loginSubmitted(self):
        c = self.parent.db.cursor()
        r = c.execute("SELECT * from tblusername WHERE username = {} and password = {}", [self.usernamebox.get(), self.passwordbox.get()])
        results = r.fetchall()
        if len(results)>0:
        #if True:
            self.feedbacklabel.config(text="")
            self.parent.successfulLogin(self.usernamebox.get())
            return True
        else:
            self.feedbacklabel.config(text="Incorrect Login")
            return False
        
