import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
import sqlite3 as sql
from LoginScreen import LoginFrame

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x600")
        self.title("Main Menu")
        self.loggedInUser = ""
        self.db = sql.connect("demoFile.sqlite")

        self.frames = [ LoginFrame(self)]

        self.switchFrame(0)

    def successfulLogin(self,username):
        self.loggedInUser = username
        print("Logged in as", username)
        self.switchFrame(1)








    
def makeDatabase(db):
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
    c.execute("CREATE TABLE tbluserdetails (firstname TEXT,surname TEXT, p
        self.switchFrame(0)
assword TEXT, userid INTEGER PRIMARY KEY AUTOINCREMENT)")
    c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("John","Smith","12345"))
    c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Bob","Patl","P4ssw0rd"))
    c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("dimon","dith","baejk"))
    c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Hahs","kyee","hashhash"))
    c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Louis","oPris","WOMPWOMP"))
    
#userstats database initialisation
    c.execute("CREATE TABLE tbluserstats (userid INTEGER,questionid INTEGER, attemptid INTEGER PRIMARY KEY AUTOINCREMENT, dateanswered TEXT, score INTEGER)")
    c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/8/6", 5))
    c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/9/6", 5))
    c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/10/6", 5))
    c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/11/6", 5))
    c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/5/12", 5))


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)




        # we can make "pages" appear and disappear by putting them into separate frames
        self.introFrame = tk.Frame(self,width=800)
        self.title = tk.Label(self.introFrame, anchor="w", justify="left", text="Welcome to my demo\nI hope you enjoy it.", bg="#FF00AA")
        self.title.grid(row=0, column=0, sticky="NSEW")
        demotextbox = tk.Text(self.introFrame, width=70, height=10, borderwidth=0)
        demotextbox.grid(row=1,column=0, sticky="NSEW")
        someText = "this is some text\nIt is very nice and it fits so well in this box"
        demotextbox.insert("end",someText)
        demotextbox.config(state = "disabled")
        self.introFrame.columnconfigure(0,weight=1)
        # we put this into the grid at the start of the program
        # so it appears first
        self.introFrame.grid(row=0, column=0,rowspan=3, sticky="NSEW") 

        # a separate frame for the second page
        self.secondFrame = tk.Frame(self,width=500)
        self.page2title = tk.Label(self.secondFrame, anchor="w", justify="left", text="This is the second page", bg="#0088AA")
        self.page2title.grid(row=0, column=0, sticky="NSEW")
        self.secondFrame.columnconfigure(0,weight=1)
        # we don't put this frame in the grid yet
        # so it doesn't appear until the button is pressed

        menubutton1 = tk.Button(self,text="Go to page 1", command = self.page1Switch)
        menubutton1.grid(row=0, column=1, sticky="NEW")
        menubutton2 = tk.Button(self,text="Go to page 2", command = self.page2Switch)
        menubutton2.grid(row=1, column=1, sticky="NEW")

        # these lines make sure that the left frame is the right size
        # and adds a new "empty" row at the bottom to takeup the extra space below the buttons
        self.columnconfigure(0,minsize=800)
        self.rowconfigure(2,weight=1)

        # connect to the database
        self.db = sql.connect("demofile.db")
        # run the procedure that generates new tables and records
        # this is just for the demo. You wouldn't make new tables every time
        makeDatabase(self.db)

        # now print out what you find in there
        self.testDB()

        # this belongs at the end of the __init__ procedure.
        # It starts the main loop which runs the tkinter window
        self.mainloop()

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

    def page1Switch(self):
        # removes other frames from the grid, but adds page 1
        self.secondFrame.grid_forget()
        self.introFrame.grid(row=0, column=0,rowspan=3, sticky="NSEW") 

    def page2Switch(self):
        # removes other frames from the grid, but adds page 2
        self.introFrame.grid_forget()
        self.secondFrame.grid(row=0, column=0,rowspan=3, sticky="NSEW") 

if __name__ == "__main__":
    app = App()

