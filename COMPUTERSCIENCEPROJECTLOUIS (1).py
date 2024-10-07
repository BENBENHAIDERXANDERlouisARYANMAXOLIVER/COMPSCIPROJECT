import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
import sqlite3 as sql
from LoginScreen import LoginFrame

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x600")
        self.title("Main Menu")
        self.loggedInUser = ""
        self.db = sql.connect("demoFile.db")

        self.makeDatabase(self.db)
        self.testDB()

        self.frames = [ LoginFrame(self)]
        self.columnconfigure(0,weight=1)
        
        self.rowconfigure(0,weight=1)
        self.switchFrame(0)

    def successfulLogin(self,username):
        self.loggedInUser = username
        print("Logged in as", username)
        self.switchFrame(0)

    def switchFrame(self, frameNum):
        # hide all frames except the one chosen
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if i == frameNum:
                frame.grid(row=0, column=0, sticky="NSWE")
                frame.loadUp()
            else:
                frame.grid_forget()

            
    def makeDatabase(self, db):
            #Database craeted and oldcopies are dropped
            c = db.cursor()
            c.execute("DROP TABLE IF EXISTS tblquestions")
            c.execute("DROP TABLE IF EXISTS tbluserdetails")
            c.execute("DROP TABLE IF EXISTS tbluserstats")
            
        
        # Question database initialisation and adding more data
            c.execute("CREATE TABLE tblquestions (questionimg TEXT, maxscore INTEGER,topicname TEXT, answer TEXT, questionid INTEGER PRIMARY KEY AUTOINCREMENT, hints TEXT, modelanswer TEXT)")
            c.execute("INSERT INTO tblquestions(Questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "Test", 5 ,"ASTRO","lightyear", "NOHINT", "TESTVALUE"))
            c.execute("INSERT INTO tblquestions(Questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "Test", 12 ,"Forces","Vector", "NOHINT", "TESTVALUE"))
            c.execute("INSERT INTO tblquestions(Questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "Test", 2 ,"Gravity","12N", "NOHINT", "TESTVALUE"))
            c.execute("INSERT INTO tblquestions(Questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "Test", 1 ,"Electricity","12V", "NOHINT", "TESTVALUE")) 
            c.execute("INSERT INTO tblquestions(Questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "Test", 5 ,"Mechanics","200N", "Units", "TESTVALUE"))
            
            
            
            db.commit()
        #userDetails database initialisation
            c.execute("CREATE TABLE tbluserdetails (firstname TEXT,surname TEXT,password TEXT, answer TEXT, userid INTEGER PRIMARY KEY AUTOINCREMENT)")
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("John","Smith","12345"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Bob","Patl","P4ssw0rd"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("dimon","dith","baejk"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Hahs","kyee","hashhash"))
            c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Hahs","kyee","hashhash"))
            
        #userstats database initialisation
            c.execute("CREATE TABLE tbluserstats (userid INTEGER,questionid INTEGER, attemptid INTEGER PRIMARY KEY AUTOINCREMENT, dateanswered TEXT, score INTEGER)")
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/8/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/9/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/10/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/11/6", 5))
            c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/5/12", 5))



    def testDB(self):
                # this just accesses the database and print out what it finds in the pupils table
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