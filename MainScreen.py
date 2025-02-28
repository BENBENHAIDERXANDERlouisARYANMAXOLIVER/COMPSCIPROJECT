import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>")


        #Canvas- physics tester logo
        self.TitleLabel = tk.Canvas(self, width=1000, height=276, bg="white", borderwidth=0, highlightthickness=0)
        self.Physicslogo= tk.PhotoImage(file="physicstesterlogo.png")
        self.TitleLabel.create_image(0,0 ,image=self.Physicslogo, anchor="nw")
        self.TitleLabel.configure(background="white")
        
            
        self.TitleLabel.grid(row=0, column=2, columnspan=2, sticky="NSWE")
        self.columnconfigure(0,minsize=400)
        self.rowconfigure(1,minsize=200)
     #start test button
        starttest=tk.Button(self, text="Start Test",bg="#5100FF",fg="white", font="Georgia", activebackground="#f1ed0e",relief="groove",command=self.startkeypressed)
        starttest.grid(row=4,column=2,columnspan=2,sticky="NSWE") 
     #settings test button
        settingsbutton=tk.Button(self, text="Settings",bg="#CCCCCC",fg="black", font="Georgia", activebackground="black",relief="groove", activeforeground="#CCCCCC")
        settingsbutton.grid(row=5,column=2,columnspan=2,sticky="NSWE") 
     
     #tiny cog canvas
     
        self.cogLabel = tk.Canvas(self, width=10, height=10, bg="white", borderwidth=0, highlightthickness=0)
        self.cogimage= tk.PhotoImage(file="COG.png")
        self.cogLabel.create_image(0,0 ,image=self.cogimage, anchor="nw")
        self.cogLabel.configure(background="white")
        self.cogLabel.grid(row=5, column=1, columnspan=1, sticky="NESW")
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
    
   
       
        
