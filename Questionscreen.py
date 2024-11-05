import tkinter as tk
import random
AnswerCorrect=False

class QuestionFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("")
        

        #random question selected
        c = self.parent.db.cursor()
        r = c.execute("SELECT * FROM tblquestions ORDER BY RANDOM() Limit 1;")
        self.RandomQ = r.fetchone()
        
        self.attempts=0
        
     #   Topic label
        topic=self.RandomQ[2]
      
       # a = c.execute("SELECT topicname FROM RandomQ" )
        
        besttopiclabel = tk.Label(self, text=topic)
        besttopiclabel.grid(row=5 ,column=0,  sticky="NSWE")
        besttopiclabel.configure(background="white")
        besttopiclabel.config(font=("Arial", 24))

        
        questionimg=self.RandomQ[0]
       #questionimg
        self.physicsquestion = tk.Canvas(self, width=1000, height=276, bg="white", borderwidth=0, highlightthickness=0)
        self.physicsquestionimg= tk.PhotoImage(file=questionimg)
        self.physicsquestion.create_image(0,0 ,image=self.physicsquestionimg, anchor="nw")
        self.physicsquestion.configure(background="white")
        self.physicsquestion.grid(row=0, column=1, columnspan=2, sticky="NSWE")


        #answerbox
        self.answerbox = tk.Entry(self,text="Enter Answer")
        self.answerbox.grid(row=6,column=1,sticky="NSEW")
        
        #question num text
      #  questionnumber=i
        questionnum = tk.Label(self, text="Q num")
        questionnum.grid(row=0, column=0, sticky="NSWE")
        questionnum.configure(background="white")
        questionnum.config(font=("Arial", 24))
        
        #hint button
        #if (self.attempts>=1):
         #   buttonstatus=tk.NORMAL
            
     #   else:
        buttonstatus=tk.DISABLED
        print(buttonstatus)
        self.hintbutton=tk.Button(self, text="hint",command=self.hintpressed, state=buttonstatus)
        self.hintbutton.grid(row=0,column=4,columnspan=1,sticky="NSWE")

       #submit button
        submitbutton=tk.Button(self, text="submit",command=self.Answerpressed)
        submitbutton.grid(row=7,column=1,columnspan=1,sticky="NSWE")







    def hintpressed(self):
        print(self.RandomQ[5])
        if (self.attempts>=1):
            buttonstatus=tk.NORMAL
        print(buttonstatus)
     






    def Answerpressed(self):
        if(self.answerbox.get()==self.RandomQ[3]):
            self.AnswerCorrect=True
            print("correct")
            self.attempts=0
        elif(self.answerbox.get()!=self.RandomQ[3]):
            print("nuh huh huh")
            self.attempts+=1
            self.hintbutton.config(state=tk.NORMAL)
         #   print(self.attempts)
        #check if entered value is accepted
        #wait a certain amount of time,
        #then switch frame 
        #add one to attempt counter
       
  #  def startkeypressed(self):
   #     self.parent.switchtoquestionscreen()
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
   
