import tkinter as tk
import sqlite3 as sql
from tkinter import font as tkFont
from tkinter import messagebox
from LoginScreen import LoginFrame
from MainScreen import MainFrame
from Questionscreen import QuestionFrame
from ReviewScreen import ReviewFrame
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x600")
        self.title("Main Menu")
        self.loggedInUser = ""
        self.db = sql.connect("demoFile.db")

        self.makeDatabase(self.db)
        self.isCorrect = False
        self.isWrong = False
        self.testDB()
        attempts=0
        self.frames = [LoginFrame(self),MainFrame(self),QuestionFrame(self), ReviewFrame(self)]
        self.columnconfigure(0,weight=1)
        
        self.rowconfigure(0,weight=1)
        self.switchFrame(0)

    def successfulLogin(self,username):
        self.loggedInUser = username
        print("Logged in as", username)
        self.switchFrame(1)
   
    def switchFrame(self, frameNum):
        # hide all frames except the one chosen
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if i == frameNum:
                frame.grid(row=0, column=0, sticky="NSWE")
                frame.loadUp()
            else:
                frame.grid_forget()
  
    def switchtoquestionscreen(self):
        self.switchFrame(2)
            

    def switchtoreviewscreen_Right(self):
        self.switchFrame(3)
        self.isCorrect=True

    def switchtoreviewscreen_Wrong(self):
        self.switchFrame(3)
        self.isWrong=True
        



    
    def makeDatabase(self, db):
            #Database created and oldcopies are dropped
            c = db.cursor()
            c.execute("DROP TABLE IF EXISTS tblquestions")
            c.execute("DROP TABLE IF EXISTS tbluserdetails")
            c.execute("DROP TABLE IF EXISTS tbluserstats")
            
        
        # Question database initialisation and adding more data
            c.execute("CREATE TABLE tblquestions (questionimg TEXT, maxscore INTEGER,topicname TEXT, answer TEXT, questionid INTEGER PRIMARY KEY AUTOINCREMENT, hints TEXT, modelanswer TEXT)")
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "physicstesterlogo.png", 5 ,"ASTRO","lightyear", "why", "TESTVALUE"))
          #  c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "physicstesterlogo.png", 12 ,"Forces","Vector", "do", "TESTVALUE"))
         #   c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "GravitykineticEnergy1markQ.png", 1 ,"Gravitational Fields","P has more kinetic energy and less potential energy than Q.", "Think how potential energy changes with distance to an object", "TESTVALUE"))
            c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "ElectricityResistanceRatio1MarkQ.png", 1 ,"Electricity","1,2,3,4,5,6,7,8", "set unchanging values to one", "TESTVALUE")) 
          #  c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "MechanicsEfficiency1mark Q.png", 1 ,"Mechanics","50%", "use P=FV", "TESTVALUE"))
            
            
            
            db.commit()
        #userDetails database initialisation
            c.execute("CREATE TABLE tbluserdetails (firstname TEXT,surname TEXT,password TEXT, answer TEXT, userid INTEGER PRIMARY KEY AUTOINCREMENT)")
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("John","Smith","12345"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Bob","Patl","P4ssw0rd"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("dimon","dith","baejk"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("1","kyee","1"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("wo","wd","Testing"))
            
        #userstats database initialisation
            c.execute("CREATE TABLE tbluserstats (userid INTEGER,questionid INTEGER, attemptid INTEGER PRIMARY KEY AUTOINCREMENT, dateanswered TEXT, score INTEGER)")
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/8/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/9/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/10/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/11/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/5/12", 5))



    def testDB(self):
                #Database accessed and all lines from data based printed out(spacing added for readability)
                c = self.db.cursor()
                results = c.execute("SELECT * FROM tblquestions")
                print("Question Table")
                for line in results.fetchall():
                    print(line) 
                for i in range (3):
                    print("")
                print("UserDetails Table")
                c = self.db.cursor()

                results = c.execute("SELECT * FROM tbluserdetails")
                for line in results.fetchall():
                    print(line)
                for i in range (3):
                    print("")
                print("UserStats Table")
                c = self.db.cursor()
                results = c.execute("SELECT * FROM tbluserstats")
            
                for line in results.fetchall():
                    print(line )
                for i in range (3):
                    print("")
                
                
            #  c=self.db.cursor()
            #  results=c.execute()



if __name__ == "__main__":
    app = App()

    app.mainloop()