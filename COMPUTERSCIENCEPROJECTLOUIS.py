from tkinter import *
import tkinter.font as tkFont
import sqlite3 as sql

    
def makeDatabase(db):
    #Database craeted and oldcopies are dropped
    c = db.cursor()
    c.execute("DROP TABLE IF EXISTS tblQuestions")
    c.execute("DROP TABLE IF EXISTS tbluserdetails")
    c.execute("DROP TABLE IF EXISTS tbluserstats")
    
  
# Question database initialisation
    c.execute("CREATE TABLE tblQuestions (Questionimg TEXT, maxscore INTEGER,TopicName TEXT, Answer TEXT, QuestionID INTEGER PRIMARY KEY AUTOINCREMENT, Hints TEXT, ModelAnswer TEXT)")
    c.execute("INSERT INTO tblQuestions(Questionimg ,maxscore,TopicName, Answer, Hints, ModelAnswer) Values (?,?,?,?,?,?)", ( "Test", 5 ,"ASTRO","lightyear", "NOHINT", "TESTVALUE"))
    db.commit()
#userDetails database initialisation
    c.execute("CREATE TABLE tbluserdetails (FirstName TEXT,Surname TEXT, Password TEXT, UserID INTEGER PRIMARY KEY AUTOINCREMENT)")
    c.execute("INSERT INTO tbluserdetails(FirstName ,Surname, Password) Values (?,?,?)", ("John","Smith","12345"))
#userstats database initialisation
    c.execute("CREATE TABLE tbluserstats (Userid INTEGER,QuestionID INTEGER, AttemptID INTEGER PRIMARY KEY AUTOINCREMENT, dateanswered INTEGER, Score INTEGER, maxscore INTEGER )")
    c.execute("INSERT INTO tbluserstats(dateanswered ,Score, maxscore) Values (?,?,?)", (21012007,5,6))


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=18)




        # we can make "pages" appear and disappear by putting them into separate frames
        self.introFrame = Frame(self,width=800)
        self.title = Label(self.introFrame, anchor="w", justify="left", text="Welcome to my demo\nI hope you enjoy it.", bg="#FF00AA")
        self.title.grid(row=0, column=0, sticky="NSEW")
        demotextbox = Text(self.introFrame, width=70, height=10, borderwidth=0)
        demotextbox.grid(row=1,column=0, sticky="NSEW")
        someText = "this is some text\nIt is very nice and it fits so well in this box"
        demotextbox.insert("end",someText)
        demotextbox.config(state = "disabled")
        self.introFrame.columnconfigure(0,weight=1)
        # we put this into the grid at the start of the program
        # so it appears first
        self.introFrame.grid(row=0, column=0,rowspan=3, sticky="NSEW") 

        # a separate frame for the second page
        self.secondFrame = Frame(self,width=500)
        self.page2title = Label(self.secondFrame, anchor="w", justify="left", text="This is the second page", bg="#0088AA")
        self.page2title.grid(row=0, column=0, sticky="NSEW")
        self.secondFrame.columnconfigure(0,weight=1)
        # we don't put this frame in the grid yet
        # so it doesn't appear until the button is pressed

        menubutton1 = Button(self,text="Go to page 1", command = self.page1Switch)
        menubutton1.grid(row=0, column=1, sticky="NEW")
        menubutton2 = Button(self,text="Go to page 2", command = self.page2Switch)
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
        results = c.execute("SELECT * FROM tblQuestions")
        for line in results.fetchall():
            print(line)
        c = self.db.cursor()
        results = c.execute("SELECT * FROM tbluserdetails")
        for line in results.fetchall():
            print(line)
        c = self.db.cursor()
        results = c.execute("SELECT * FROM tbluserstats")
       
        for line in results.fetchall():
            print(line )


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