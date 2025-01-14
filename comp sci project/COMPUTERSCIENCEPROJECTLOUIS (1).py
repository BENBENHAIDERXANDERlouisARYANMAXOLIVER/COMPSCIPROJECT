import tkinter as tk
import sqlite3 as sql
from tkinter import font as tkFont
from tkinter import messagebox
from LoginScreen import LoginFrame
from MainScreen import MainFrame
from Questionscreen import QuestionFrame
from ReviewScreen import ReviewFrame
from takedata import dataFrame
from SettingsScreen import SettingsFrame
from AccountDeleteScreen import DeleteFrame
from statsscreen import StatsFrame
from datetime import datetime,timedelta
from collections import defaultdict

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x600")
        self.title("Main Menu")
        self.loggedInUser = ""
        self.db = sql.connect("demoFile.db")
        self.magnetism=0
        self.electricity=0
        self.Nuclear=0
        self.further_mechanics=0
        self.gravity=0
        self.prohibitedtopics=[]
        self.hintstate=1
        self.topicbuttonstate=1
        self.activatestats=False

    








        self.makeDatabase(self.db)
        self.AnswerCorrect=True
        self.testDB()
        attempts=0
        self.frames = [LoginFrame(self),MainFrame(self),QuestionFrame(self), ReviewFrame(self),SettingsFrame(self),DeleteFrame(self),StatsFrame(self)]
        #LoginFrame(self),MainFrame(self),QuestionFrame(self), ReviewFrame(self),
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
    
    def switchtomainscreen(self):
        self.switchFrame(1)
    
    def switchtodeleteFrame(self):
        self.switchFrame(5)
    
    def switchtostatsFrame(self):
        self.switchFrame(6)
        self.activatestats=True

    def switchtoreviewscreen_Right(self):
        self.switchFrame(3)
        self.AnswerCorrect=True
        print("this is right")

    def switchtoreviewscreen_Wrong(self):
        self.switchFrame(3)
        self.AnswerCorrect=False
        print("this is wrong")
    
    def switchtosettings(self):
        self.switchFrame(4)
    def overall_topic_scoring(self,arrayname,Topic):
        TempScore=1
        TempQuestionsAnswered=0
        c = self.db.cursor()
        r = c.execute("SELECT userid FROM tbluserdetails WHERE firstname = ?  ", [self.loggedInUser])
        Founduserid=r.fetchone()
       # print(Founduserid)
        #print("#####FIRST TEST< SHOOULD RETURN 1")
        #Test passed
    #works fine
        print("####")
        print(Topic)
        print("Electricity")

        a = c.execute("SELECT questionid FROM tblquestions WHERE topicname = ? ", [Topic])
        Topic_of_question=a.fetchall()
        print(Topic_of_question)
        print("###### THIS SHOULD PRINT only one question ID (2)")
        
        #thisworks fine but printts onlu one question id, you need to fetcahll for teh scores
    
        for item in Topic_of_question:
            print(item[0])
            print("############### THIS IS THE ITEM[0]")
            print(Founduserid[0])



            a = c.execute("SELECT score FROM tbluserstats WHERE questionid = ? AND  userid = ? ", [item[0],Founduserid[0]])
            thescores=r.fetchall()
            print(thescores)
            print("################## THIS SHOULD PRINT A LOT OF SCORES")
            for item in thescores:

                
                if thescores[0][0]>0:
                    TempScore+=1
                TempQuestionsAnswered+=1
        if TempQuestionsAnswered>0:
            arrayname=TempScore/TempQuestionsAnswered
        else:
            arrayname=TempScore/10000
        print(arrayname)
        print("#######################3")
        return arrayname
        

    def Weekly_topic_scoring(self,arrayname,Topic):
        TempScore=1
        TempQuestionsAnswered=0
        thecurrentdate=datetime.now()
        oneweekago=thecurrentdate-timedelta(days=7)
        c = self.db.cursor()
        r = c.execute("SELECT userid FROM tbluserdetails WHERE firstname = ?  ", [self.loggedInUser])
        Founduserid=r.fetchone()
       # print(Founduserid)
        #print("#####FIRST TEST< SHOOULD RETURN 1")
        #Test passed
    #works fine
        print("####")
        print(Topic)
        print("Electricity")

        a = c.execute("SELECT questionid FROM tblquestions WHERE topicname = ? ", [Topic])
        Topic_of_question=a.fetchall()
        print(Topic_of_question)
        print("###### THIS SHOULD PRINT only one question ID (2)")
        
        #thisworks fine but printts onlu one question id, you need to fetcahll for teh scores
    
        for item in Topic_of_question:
            print(item[0])
            print("############### THIS IS THE ITEM[0]")
            print(Founduserid[0])



            a = c.execute("SELECT score FROM tbluserstats WHERE questionid = ? AND  userid = ? AND dateanswered > ? ", [item[0],Founduserid[0],oneweekago])
            thescores=r.fetchall()
            print(thescores)
            print("################## THIS SHOULD PRINT A Few")
            for item in thescores:

                
                if thescores[0][0]>0:
                    TempScore+=1
                TempQuestionsAnswered+=1
        if TempQuestionsAnswered>0:
            arrayname=TempScore/TempQuestionsAnswered
        else:
            arrayname=TempScore/10000
        print(arrayname)
        print("#######################3")
        return arrayname
        
    

        

                

            
        
            
                
            

       
        
#element.grid_forget()


    
    def makeDatabase(self, db):
            #Database created and oldcopies are dropped
            c = db.cursor()
            #c.execute("DROP TABLE IF EXISTS tblquestions")
           # c.execute("DROP TABLE IF EXISTS tbluserdetails")
          #  c.execute("DROP TABLE IF EXISTS tbluserstats")
            
        
        # Question database initialisation and adding more data
           
            #c.execute("CREATE TABLE tblquestions (questionimg TEXT, maxscore INTEGER,topicname TEXT, answer TEXT, questionid INTEGER PRIMARY KEY AUTOINCREMENT, hints TEXT, modelanswer TEXT)")
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "ParticlesCharge1markQ.png", 1 ,"Particles","Alpha particle, alpha particle", "Consider the relative  charge of the particles and  how they relate to each other and times by voltage", "ParticlesCharge1markQ.png"))
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "WavesSonar1markQ.png", 1 ,"Waves","2.25m, 2.25 meters", "Remember that each pulse contains 12 oscillations", "WavesSonar1markQ.png"))
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "GravitykineticEnergy1markQ.png", 1 ,"Gravity","P has more kinetic energy and less potential energy than Q.", "Think how potential energy changes with distance to an object", "GravitykineticEnergy1markQ.png"))
            #c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "ElectricityResistanceRatio1MarkQ.png", 1 ,"Electricity","1,2,3,4,5,6,7,8", "set unchanging values to one", "ElectricityResistanceRatio1MarkQ.png")) 
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "MechanicsEfficiency1mark Q.png", 1 ,"Mechanics","50%", "use P=FV", "MechanicsEfficiency1mark Q.png"))
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "WavesFirstHarmonictension1markQ.png", 1 ,"Waves","420hz", "Use The tension and frequency equation, and set any unchanged values to one", "WavesFirstHarmonictension1markQ.png"))
            #c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "FurtherMechanicsSHMAngularspeed1mark.png", 1 ,"FurtherMechanics","150 rad s−1, 150rads/s , 150 rad/scond, 150 rads^-1", "Convert speed to SL units", "FurtherMechanicsSHMAngularspeed1mark.png")) 
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "NuclearHalflife1markQ.png", 1 ,"Nuclear","3000", "Sub the activity equation into the halflife equation", "NuclearHalflife1markQ.png")) 
           # c.execute("INSERT INTO tblquestions(questionimg ,maxscore,topicName, answer, hints, modelanswer) Values (?,?,?,?,?,?)", ( "Magnetismpurpendicularqmark.png", 1 ,"Magnetism","a uniform magnetic field,a,A", "Use Flemmings Left hand rule", "Magnetismpurpendicularqmark.png")) 
            
           
        #userDetails database initialisation
           # c.execute("CREATE TABLE tbluserdetails (firstname TEXT,surname TEXT,password TEXT, answer TEXT, userid INTEGER PRIMARY KEY AUTOINCREMENT)")
            #c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("John","Smith","12345"))
           # c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("Bob","Patl","P4ssw0rd"))
           # c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("dimon","dith","baejk"))
           # c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("1","kyee","1"))
           # c.execute("INSERT INTO tbluserdetails(firstname ,surname, password) Values (?,?,?)", ("wo","wd","Testing"))
            #db.commit()
        #userstats database initialisation
         #   c.execute("CREATE TABLE tbluserstats (userid INTEGER,questionid INTEGER, attemptid INTEGER PRIMARY KEY AUTOINCREMENT, dateanswered TEXT, score INTEGER)")
          #  c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/8/6", 5))
           # c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/9/6", 5))
           # c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/10/6", 5))
            #c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/11/6", 5))
            #c.execute("INSERT INTO tbluserstats( userid, questionid,  dateanswered ,score) Values (?,?,?,?)", (None, None,"2024/5/12", 5))
            db.commit()


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
                results = c.execute("SELECT * FROM tbluserstats")
                for line in results.fetchall():
                    print(line)
                
                
                
                
            #  c=self.db.cursor()
            #  results=c.execute()



if __name__ == "__main__":
    app = App()

    app.mainloop()


    #questionList = []

#topics = ["Magnetism", "Nuclear", "Electronics"]

#for topicNum in range(12):
	#if self.checked[topicNum] == 1:		
	##	result = c.execute("SELECT * FROM tblQuestions WHERE Topic = ?", (topics[topicNum,))
	#	qs = result.fetchall()
	#	questionList = questionList + qs
