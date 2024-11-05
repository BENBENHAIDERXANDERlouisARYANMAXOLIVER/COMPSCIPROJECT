import tkinter as tk
import random
class QuestionFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>")


        #Catagory label
        c = self.parent.db.cursor()
        r = c.execute("SELECT topicName FROM tblquestions ORDER BY RANDOM() Limit 1;")
        print(r)
        besttopiclabel = tk.Label(self, text="")
        besttopiclabel.grid(row=2 ,column=2, columnspan=1, sticky="NSWE")
        besttopiclabel.configure(background="white")
        besttopiclabel.config(font=("Arial", 24))

        
     #start test button
        starttest=tk.Button(self, text="Start Test",bg="#5100FF",fg="white", font="Georgia", activebackground="#f1ed0e",relief="groove",command=self.startkeypressed)
        starttest.grid(row=4,column=2,columnspan=1,sticky="NSWE") 
     #settings test button
        settingsbutton=tk.Button(self, text="Settings",bg="#CCCCCC",fg="black", font="Georgia", activebackground="black",relief="groove", activeforeground="#CCCCCC")
        settingsbutton.grid(row=5,column=2,columnspan=1,sticky="NSWE") 
     
     #tiny cog canvas
     
        self.cogLabel = tk.Canvas(self, width=10, height=10, bg="white", borderwidth=0, highlightthickness=0)
        self.cogimage= tk.PhotoImage(file="COG.png")
        self.cogLabel.create_image(0,0 ,image=self.cogimage, anchor="nw")
        self.cogLabel.configure(background="white")
        self.cogLabel.grid(row=5, column=1, columnspan=1, sticky="E")
        self.columnconfigure(1,minsize=50)
     
     #user stats label b
        besttopiclabel = tk.Label(self, text="Best Topic : ")
        besttopiclabel.grid(row=2 ,column=2, columnspan=1, sticky="NSWE")
        besttopiclabel.configure(background="white")
        besttopiclabel.config(font=("Arial", 24))


     #user stats label w
        worsttopiclabel = tk.Label(self, text="Worst Topic : ")
        worsttopiclabel.grid(row=3, column=2, columnspan=1, sticky="NSWE")
        worsttopiclabel.configure(background="white")
        worsttopiclabel.config(font=("Arial", 24))







       
    def startkeypressed(self):
        self.parent.switchtoquestionscreen()
        # they pressed return. have they entered a username yet?
   #     if len(self.usernamebox.get())>0:
  #          self.loginSubmitted()

    def loadUp(self):
        print("loaded Login")
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
        
