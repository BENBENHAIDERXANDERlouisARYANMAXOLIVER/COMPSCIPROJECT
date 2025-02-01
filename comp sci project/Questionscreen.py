import tkinter as tk
import random
import time
from datetime import datetime,timedelta
AnswerCorrect=False


#issues: when this frame is updated the main program refuses to recgnise the update
#tblquestions[4]is the question ID tbluserdetails[4] is the user ID
#changes to page layout: spacea added above question, and below


class QuestionFrame(tk.Frame):
    def __init__(self, parent):
        
        
       
        self.Question_Restarted=False
        self.QuestionsAnswered=0
        self.parent = parent
        self.db = parent.db
        self.QuestionsCorrect=0
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("")
        self.parent.bind("<s>", self.parent.switchtosettings)
        self.questionsSelected=[]
        self.keep_finding_new_questions=True
        self.columnconfigure(0,minsize=400)
        self.rowconfigure(0,minsize=90)
        self.rowconfigure(2,minsize=90)
        self.marks=0
        self.QuestionArray=[]
        self.final_question_array_with_weighting=[('ElectricityResistanceRatio1MarkQ.png', 1, 'Electricity', '1,2,3,4,5,6,7', 1, 'set unchanging values to one', 'ElectricityResistanceRatio1MarkQ.png'),('GravitykineticEnergy1markQ.png', 1, 'Gravity', 'P has more kinetic energy and less potential energy than Q.', 1, 'Think how potential energy changes with distance to an object', 'GravitykineticEnergy1markQ.png') ,('FurtherMechanicsSHMAngularspeed1mark.png', 1, 'Further Mechanics', '150 rad s−1, 150rads/s , 150 rad/scond, 150 rads^-1', 3, 'Convert speed to SL units', 'FurtherMechanicsSHMAngularspeed1mark.png') ]
        self.ListOfQuestionIDs=[1,2,3,4,5,6]
        self.FMechanicsArray=[]
        self.Gravity_Array=[]
        self.Nuclear_Array=[]
        self.Electricity_Array=[]
        self.Magnetism_Array=[]
        self.temparray=[]
        #weighting variables
        self.FMechanics_Weight=5
        self.Gravity_Weight=5
        self.Nuclear_Weight=5
        self.Electricity_Weight=5
        self.Magnetism_Weight=5
        self.firstQ=0
        #start test button
        self.is_prohib_topic=0       
        self.sTestbutton=tk.Button(self, text="submit",command=self.Begin_Test)
        self.sTestbutton.grid(row=9,column=2,columnspan=4,rowspan=3,sticky="NSWE")
       
 








       
        

    def Begin_Test(self):
        self.sTestbutton.grid_forget()


        self.userID=self.parent.loggedInUser
        c = self.parent.db.cursor()
        #further mechanics
        r = c.execute("SELECT * FROM tbluserstats WHERE userid=? ",[self.userID])
        self.QuestionArray = r.fetchall()
        
        
        #Electricity
        r = c.execute("SELECT * FROM tbluserstats WHERE userid=? ",[self.userID])
        self.QuestionArray = r.fetchall()
        
       

        tempvar=0
        random_minus=(len(self.final_question_array_with_weighting))
       
        the_Random_Q=random.randint(1,random_minus-1)
        self.RandomQ=self.final_question_array_with_weighting[the_Random_Q]
        
        
       
        
        print("############################################################")
        print(self.parent.prohibitedtopics)
        print("############################################################")
        
        for item in self.parent.prohibitedtopics:
            if item==self.RandomQ[2]:
                self.is_prohib_topic=1
        while(self.is_prohib_topic==1):
            self.is_prohib_topic=0
            random_minus=(len(self.final_question_array_with_weighting))
            # print(random_minus)
            the_Random_Q=random.randint(1,random_minus-1)
            self.RandomQ=self.final_question_array_with_weighting[the_Random_Q]
            for topic in self.parent.prohibitedtopics:
                if topic==self.RandomQ[2]:
                    self.is_prohib_topic=1
        self.questionsSelected.append(self.RandomQ[0][4])


        
        


        

        
        
        
            






        
        


        #random question selected
        c = self.parent.db.cursor()
       # r = c.execute("SELECT * FROM tblquestions ORDER BY RANDOM() Limit 1;")
       # self.RandomQ = r.fetchone()
       # self.questionsSelected.append(self.RandomQ[4])
        self.attempts=0




       # self.Actualpercentages(self.FMechanics_Weight,self.FMechanics_Weight)
        #self.Actualpercentages( self.Gravity_Array, self.Gravity_Weight)
        #self.Actualpercentages(self.Nuclear_Array, self.Nuclear_Weight)
        #self.Actualpercentages( self.Electricity_Array,self.Electricity_Weight)
        #self.Actualpercentages( self.Magnetism_Array, self.Magnetism_Weight)

        
            

        
        #find array length
       #look at all items[4] then 100/(item[all item 4s ( for loop)] /array length * 100
       #roud that number to 2.dp
       #create an array for the amount of weights in teh weightig variables 
       # then for every single topic for i in range(the weighting number for teh given topic):
       #
    # pick a random question

       #put it into an array a certain amount of times depending on teh nuebr , e.g base num =1

       #e.g











        
     #   Topic label
        topic=self.RandomQ[0][2]
      
       # a = c.execute("SELECT topicname FROM RandomQ" )
        if(self.parent.topicbuttonstate==0):
            topic= "TOPICS DISABLED"
        else:

            topic=self.RandomQ[0][2]
        self.besttopiclabel = tk.Label(self, text=topic)
        self.besttopiclabel.grid(row=7 ,column=1,  sticky="NSWE")
        self.besttopiclabel.configure(background="white")
        self.besttopiclabel.config(font=("Arial", 24))

        
        questionimg=self.RandomQ[0][0]
       #questionimg
        self.physicsquestion = tk.Canvas(self, width=1000, height=276, bg="white", borderwidth=0, highlightthickness=0)
        self.physicsquestionimg= tk.PhotoImage(file=questionimg)
        self.physicsquestion.create_image(0,0 ,image=self.physicsquestionimg, anchor="nw")
        self.physicsquestion.configure(background="white")
        self.physicsquestion.grid(row=1, column=2, columnspan=2, sticky="NSWE")


        #answerbox
        self.answerbox = tk.Entry(self,text="Enter Answer")
        self.answerbox.grid(row=8,column=2,sticky="NSEW")
        
        #question num text
      #  questionnumber=i
        self.questionnum = tk.Label(self, text="Q num")
        self.questionnum.grid(row=0, column=1, sticky="NSWE")
        self.questionnum.configure(background="white")
        self.questionnum.config(font=("Arial", 24))
        
        #hint button
       
        if (self.attempts>=1 and self.parent.hintstate!=0):
            self.hintbuttonstatus=tk.NORMAL
            #hint state is set to the right number
        else:

            self.hintbuttonstatus=tk.DISABLED
        print(self.hintbuttonstatus)
        self.hintbuttonimage= tk.PhotoImage(file="hintbutton.png")
        self.hintbutton=tk.Button(self, text="hint",command=self.hintpressed, state=self.hintbuttonstatus,image=self.hintbuttonimage)
        self.hintbutton.grid(row=1,column=4,columnspan=1,sticky="NSWE")

       #submit button
        self.submitbutton=tk.Button(self, text="submit",command=self.Answerpressed)
        self.submitbutton.grid(row=9,column=2,columnspan=1,sticky="NSWE")

        self.textcolor="Red"
        self.textcontents=""
        #question C/W label
        self.right_or_wrong = tk.Label(self, text=" ",fg=self.textcolor)
        self.right_or_wrong.grid(row=10, column=2, sticky="NSWE")
        self.right_or_wrong.configure(background="white")
        self.right_or_wrong.config(font=("Georgia", 24))




    def hintpressed(self):
        print(self.RandomQ[5])
        if(self.parent.hintstate==0):
            self.hintbutton.config(state=tk.DISABLED)
        
            
  
    def Questionpercentworkout(self,topic,arrayname):
        self.userID=self.parent.loggedInUser
        c = self.parent.db.cursor()
        r = c.execute("SELECT * FROM tbluserstats WHERE userid=? ",[self.userID])
        self.QuestionArray = r.fetchall()
       
        
        
        r = c.execute("SELECT questionid FROM tblquestions WHERE topicName=? ",[topic])
        self.ListOfQuestionIDs = r.fetchall()

        #this all works and a valid array is beign output
        
        for QuestionID in self.ListOfQuestionIDs:
            for item in self.QuestionArray:
                if item[1]==QuestionID[0]:
                    
                    arrayname.append(item)
                  #  print(arrayname)
                  #  print("THE ABOVE IS IN " + topic)
                    
       # print("THIS IS THE QUESTION PERCENT WORKOUT SUBPROGRAM")
                    
       
        #this all works and a valid array is beign output
        #length pf array is defined
                


    def Actualpercentages(self,Topic_Weight_Var,arrayname):
        total=0
        Arraylength=len(arrayname)
        if(Arraylength==0):
            Arraylength=1
        for item in arrayname:
            total=total+item[4]
        if total >0:
            weightingvariable=((Arraylength/total)*10)
        else:
            weightingvariable=50
        Topic_Weight_Var=round(weightingvariable)
        print("THE QUESTION WEIGHTING is"+str(Topic_Weight_Var))
        
        return Topic_Weight_Var
        print("THIS IS THE ACTUAL PERCENTAGES SUBPROGRAM")
#len of arrayname workig here
    def lengthofarray(self,arrayname):
        print("GRAVITY")
        print(self.Gravity_Array)
        print("Electricity")
        print(self.Electricity_Array)
        print("MAGNETISM")
        print(self.Magnetism_Array)
        print("Nuclear")
        print(self.Nuclear_Array)


    def GenerateQuestion(self,Topic_Weight,TheArrayName,topic):
        
        #testing
        print (topic)
       # print(arrayname)
        print("THIS IS THE LENGTH OF THE ARRAYNAME "+str(len(TheArrayName)))
        #Topic_weight is valid
        for i in range (Topic_Weight):
           
            arraynamelength=len(TheArrayName)
            if(arraynamelength==0):
                print("error: Array wrong length")
            else:
                Adjustedarraylen=arraynamelength-1

                QtoADD=random.randint(0,Adjustedarraylen)
                print(QtoADD)
              #  print("ABOVE is QUESTION TO ADD")
               # print(TheArrayName[QtoADD])
                self.temparray.append(TheArrayName[QtoADD])
                #print(self.final_question_array_with_weighting)
        




   
        
        
     

    

       #find array length
       #look at all items[4] then 100/(item[all item 4s ( for loop)] /array length * 100
       #roud that number to 2.dp
       #create an array for the amount of weights in teh weightig variables 
       # then for every single topic for i in range(the weighting number for teh given topic):
       #
    # pick a random question

       #put it into an array a certain amount of times depending on teh nuebr , e.g base num =1

       #e.g

       
       
       
       
    #    self.FMechanicsArray=[]
       # self.Gravity_Array=[]
     #   self.Nuclear_Array=[]
      #  self.Electricity_Array=[]
      #  self.magnetism_Array=[]

        






        
    
        



  



    def loadUp(self):
             #  self.Questionpercentworkout("Further mechanics",self.FMechanicsArray)
        self.Questionpercentworkout("Magnetism",self.Magnetism_Array)
        self.Questionpercentworkout("Gravity",self.Gravity_Array)
        self.Questionpercentworkout("Electricity",self.Electricity_Array)
        self.Questionpercentworkout("Nuclear",self.Nuclear_Array)
       
        #self.Actualpercentages(self.FMechanics_Weight,self.FMechanicsArray)
        self.Gravity_Weight=self.Actualpercentages(self.Gravity_Weight,self.Gravity_Array)
        self.Nuclear_Weight=self.Actualpercentages(self.Nuclear_Weight ,self.Nuclear_Array)
        self.Electricity_Weight=self.Actualpercentages(self.Electricity_Weight,self.Electricity_Array)
        self.Magnetism_Weight=self.Actualpercentages(self.Magnetism_Weight,self.Magnetism_Array)


    

        print(self.FMechanics_Weight)
        print(self.Gravity_Weight)
        print(self.Nuclear_Weight)
        print(self.Electricity_Weight)
        print(self.Magnetism_Weight)
       # self.GenerateQuestion(self.FMechanics_Weight,self.FMechanicsArray,"Further Mechanics")
        self.GenerateQuestion(self.Gravity_Weight,self.Gravity_Array,"Gravity")
        self.GenerateQuestion(self.Nuclear_Weight ,self.Nuclear_Array,"Nuclear")   
        self.GenerateQuestion(self.Electricity_Weight,self.Electricity_Array,"Electricity")
        self.GenerateQuestion(self.Magnetism_Weight,self.Magnetism_Array,"Magnetism")

        print("THE QUESTION WEIGHTING FOR Gravity IS " +str(self.Gravity_Weight))
        print("THE QUESTION WEIGHTING FOR Nuclear IS " +str(self.Nuclear_Weight))
        print("THE QUESTION WEIGHTING FOR Electricity IS " +str(self.Electricity_Weight))
        print("THE QUESTION WEIGHTING FOR magnetism IS " +str(self.Magnetism_Weight))
        print("##################################################### WEIGHTS")
       
        for item in self.temparray:
            c = self.parent.db.cursor()
            r = c.execute("SELECT * FROM tblquestions WHERE questionid=?",[item[1]])
            Appendto=r.fetchall()
            #append to
            self.final_question_array_with_weighting.append(Appendto)
      #  print(self.final_question_array_with_weighting)
        print("############# THIS IS THE FINAL QUESTION ARRAY WITH WEIGHTING")
        for item in self.final_question_array_with_weighting:
            print(item[0][2])
            

    def Answerpressed(self):
        isAnswerinRange=False
        correctAnswers = self.RandomQ[3].split(",")
      #  print(correctAnswers)
        for item in correctAnswers:
            if(self.answerbox.get().upper ==item.upper):
                isAnswerinRange=True
              


        if( isAnswerinRange==True):
            self.AnswerCorrect=True
            print(self.AnswerCorrect)
            print("SHOULD SAY TRUE ########")
            #print("correcta")

            self.attempts=0
            self.right_or_wrong.config(fg="Green",text="Correct")
            self.thetext="Correct"
            self.textcolor="Green"
            time.sleep(0.5) 
            self.QuestionReview( self.AnswerCorrect)
           # if(QuestionRestarted)
            
        elif( isAnswerinRange==False):
            
            self.textcontents="Wrong"
            self.attempts+=1
            self.hintbutton.config(state=tk.NORMAL)
            self.right_or_wrong.config(fg="Red",text="Incorrect")
            self.thetext="incorrect"
            if self.attempts>=3:
                self.QuestionReview( self.AnswerCorrect)
    #loadup review section            





     #   self.hintbutton.config(state=tk.DISABLED)
        time.sleep(0.5)
      #  self.hintbutton.config(state=tk.NORMAL)
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

   # def TestCommand(self):
  #    print("Testing")
    
    
    
    def restartQuestion(self):
        
    
    #    self.right_or_wrong_review.grid_forget()
        self.model_answer.grid_forget()
        self.correct_answer_label.grid_forget()
        self.tryagain.grid_forget()
        self.nextQ.grid_forget()
    
        self.Question_Restarted=True


     #   Topic label
        if(self.parent.topicbuttonstate==0):
              topic= "TOPICS DISABLED"
        else:
            print("#########0"+self.RandomQ)
            topic=self.RandomQ[2]
       
      
       # a = c.execute("SELECT topicname FROM RandomQ" )
        
        self.besttopiclabel = tk.Label(self, text=topic)
        self.besttopiclabel.grid(row=7 ,column=0,  sticky="NSWE")
        self.besttopiclabel.configure(background="white")
        self.besttopiclabel.config(font=("Arial", 24))

        
        questionimg=self.RandomQ[0]
       #questionimg
        self.physicsquestion = tk.Canvas(self, width=1000, height=276, bg="white", borderwidth=0, highlightthickness=0)
        self.physicsquestionimg= tk.PhotoImage(file=questionimg)
        self.physicsquestion.create_image(0,0 ,image=self.physicsquestionimg, anchor="nw")
        self.physicsquestion.configure(background="white")
        self.physicsquestion.grid(row=1, column=2, columnspan=2, sticky="NSWE")


        #answerbox
        self.answerbox = tk.Entry(self,text="Enter Answer")
        self.answerbox.grid(row=8,column=2,sticky="NSEW")
        
        #question num text
      #  questionnumber=i
        self.questionnum = tk.Label(self, text="Q num")
        self.questionnum.grid(row=0, column=1, sticky="NSWE")
        self.questionnum.configure(background="white")
        self.questionnum.config(font=("Arial", 24))
        
        #hint button
        if (self.attempts>=1):
            hintbuttonstatus=tk.NORMAL
            
        else:
            hintbuttonstatus=tk.DISABLED
            print(hintbuttonstatus)
            self.hintbuttonimage= tk.PhotoImage(file="hintbutton.png")
            self.hintbutton=tk.Button(self, text="hint",command=self.hintpressed, state=hintbuttonstatus,image=self.hintbuttonimage)
            self.hintbutton.grid(row=1,column=3,columnspan=1,sticky="NSWE")

       #submit button
        self.submitbutton=tk.Button(self, text="submit",command=self.Answerpressed)
        self.submitbutton.grid(row=9,column=2,columnspan=1,sticky="NSWE")

        self.textcolor="Red"
        self.textcontents=""
        #question C/W label
        self.right_or_wrong = tk.Label(self, text=" ",fg=self.textcolor)
        self.right_or_wrong.grid(row=10, column=2, sticky="NSWE")
        self.right_or_wrong.configure(background="white")
        self.right_or_wrong.config(font=("Georgia", 24))




   # def hintpressed(self):
  #      print(self.RandomQ[5])
  #      if (self.attempts>=1):
 #           buttonstatus=tk.NORMAL
      #  print(buttonstatus)
  
         

        



    def Answerpressed(self):
        isAnswerinRange=False
        correctAnswers = self.RandomQ[0][3].split(",")
        
        for item in correctAnswers:
            if(self.answerbox.get()==item):
                isAnswerinRange=True
              


        if( isAnswerinRange==True):
            self.AnswerCorrect=True
            print("#]##]--=-===-")
            print(self.AnswerCorrect)
            print("#]##]--=-===-")
            print("correct")
            self.attempts=0
            self.right_or_wrong.config(fg="Green",text="Correct")
            self.thetext="Correct"
            self.textcolor="Green"
            time.sleep(0.5) 
            self.QuestionReview(self.AnswerCorrect)
            
            if (self.Question_Restarted==False):
                self.QuestionsAnswered +=1
                
                self.QuestionsCorrect+=1
                
            
        elif( isAnswerinRange==False):
            self.AnswerCorrect=False
            self.textcontents="Wrong"
            self.attempts+=1
            if(self.parent.hintstate==1):

                self.hintbutton.config(state=tk.NORMAL)
            self.right_or_wrong.config(fg="Red",text="Incorrect")
            self.thetext="incorrect"
            if self.attempts>=3:
                self.QuestionReview(self.AnswerCorrect)
            
            if (self.Question_Restarted==False and self.attempts<2):
                self.QuestionsAnswered +=1
                print()
            self.answerbox.delete(0,tk.END)
         
        self.userID=  self.parent.loggedInUser
        self.questionID=(int(self.RandomQ[0][4]) +1)
        self.current_time=datetime.now()

      #  if(self.attempts<2):

        
    #fields needed: (userID,QuestionID,date answered,score)
    
    
    
    #loadup review section            
            




     #   self.hintbutton.config(state=tk.DISABLED)
        time.sleep(0.5)
      #  self.hintbutton.config(state=tk.NORMAL)
         #   print(self.attempts)
        #check if entered value is accepted
        #wait a certain amount of time,
        #then switch frame 
        #add one to attempt counter
   
   
   
   
   
   
   
   
   
   
    def QuestionReview(self, AnswerCorrect):
        #remving question parts of screen
        self.firstQ=self.firstQ+1
        self.hintbutton.grid_forget()
        self.submitbutton.grid_forget()
        self.physicsquestion.grid_forget()
        self.besttopiclabel.grid_forget()
        self.answerbox.grid_forget()
        self.questionnum.grid_forget()
        self.questionnum.grid_forget()
        self.right_or_wrong.grid_forget()


 

        
       # for i in range(10):
          #  print(" ")
           # print(self.final_question_array_with_weighting)
        print(self.RandomQ)
        print("############### RANDOM Q")
        if(self.firstQ<2):
            print("h")


           # self.questionID=(int(self.RandomQ[4]) +1)
        else:
            self.questionID=(int(self.RandomQ[0][4]) +1)
        self.current_time=datetime.now()
        c = self.parent.db.cursor()
        print("###############")
        print(AnswerCorrect)
        print("###################")
        if AnswerCorrect==True:
        

            self.marks=1
        r = c.execute("INSERT INTO  tbluserstats (userid,questionid,dateanswered,score) VALUES (?,?,?,?)" ,[self.userID, self.questionID,self.current_time,self.marks])
        self.parent.db.commit()
        self.marks=0
        
        self.userID=self.parent.loggedInUser
        c = self.parent.db.cursor()
        r = c.execute("SELECT * FROM tbluserstats WHERE userid=? ",[self.userID])
        self.Test = r.fetchall()
       # print(self.Test)
          
        #if correct text
        self.right_or_wrong_review = tk.Label(self, text=self.thetext,fg=self.textcolor)
        self.right_or_wrong_review.grid(row=1, column=2, sticky="NSWE")
        self.right_or_wrong_review.configure(background="white")
        self.right_or_wrong_review.config(font=("Georgia", 24))

        #modelAnswer
        if(self.firstQ<2):

            model_answerimg=self.RandomQ[0][6]
        else:
            model_answerimg=self.RandomQ[0][6]

       
        self.model_answer = tk.Canvas(self, width=1000, height=256, bg="white", borderwidth=0, highlightthickness=0)
        self.model_answerimg= tk.PhotoImage(file=model_answerimg)
        self.model_answer.create_image(0,0 ,image=self.model_answerimg, anchor="nw")
        self.model_answer.configure(background="white")
        self.model_answer.grid(row=2, column=2, columnspan=2, sticky="NSWE")
        if(self.firstQ<2):
            CorrectAnswer=self.RandomQ[0][3]
        else:
            CorrectAnswer=self.RandomQ[0][3]

        #Answer Label
        self.correct_answer_label = tk.Label(self, text="The List of Correct Answers are :"+ CorrectAnswer)
        self.correct_answer_label.grid(row=5, column=2, sticky="NSWE")
        self.correct_answer_label.configure(background="white")
        self.correct_answer_label.config(font=("Georgia", 24))


        #try again button
        self.tryagain=tk.Button(self, text="try again",command=self.restartQuestion)
        self.tryagain.grid(row=5,column=1,columnspan=1,sticky="NSWE")
       
        #next question button

        self.nextQ=tk.Button(self, text="next Q",command=self.NextQuestion)
        self.nextQ.grid(row=5,column=3,sticky="NSWE")



        # print("Bypassed login")
        # self.controller.successfulLogin("asmith")
  




   







    def NextQuestion(self):
        self.keep_finding_new_questions=True
        


        self.model_answer.grid_forget()
        self.correct_answer_label.grid_forget()
        self.tryagain.grid_forget()
        self.nextQ.grid_forget()
        
        if(self.QuestionsAnswered<5):
            
            while (self.keep_finding_new_questions==True):
                self.keep_finding_new_questions=False
                

                c = self.parent.db.cursor()
                r = c.execute("SELECT * FROM tblquestions ORDER BY RANDOM() Limit 1;")
                self.RandomQ = r.fetchone()
                for item in self.questionsSelected:
                    if item == self.RandomQ[4]:
                        self.keep_finding_new_questions=True
            tempvar=0
            random_minus=(len(self.final_question_array_with_weighting))
            # print(random_minus)
            the_Random_Q=random.randint(1,random_minus-1)
            self.RandomQ=self.final_question_array_with_weighting[the_Random_Q]
        
        
       
        
            print("############################################################")
            print(self.parent.prohibitedtopics)
            print("############################################################")
            print(self.RandomQ)
            print(self.RandomQ[0][2])
            for item in self.parent.prohibitedtopics:
               
                if item==self.RandomQ[0][2]:
                    tempvar=1
            while(tempvar==1):
                tempvar=0
                random_minus=(len(self.final_question_array_with_weighting))
            # print(random_minus)
                the_Random_Q=random.randint(1,random_minus-1)
                self.RandomQ=self.final_question_array_with_weighting[the_Random_Q]
                for item in self.parent.prohibitedtopics:
                    if item==self.RandomQ[0][2]:
                        tempvar=1
            
               











            self.questionsSelected.append(self.RandomQ[0][4])

                 
                
               
                

            self.attempts=0
        
     #   Topic label
            
      
       # a = c.execute("SELECT topicname FROM RandomQ" )
            if(self.parent.topicbuttonstate==0):
                topic= ("TOPICS DISABLED")
            else:
                print(self.RandomQ)
                topic=self.RandomQ[2]
            self.besttopiclabel = tk.Label(self, text=topic)
            self.besttopiclabel.grid(row=5 ,column=1,  sticky="NSWE")
            self.besttopiclabel.configure(background="white")
            self.besttopiclabel.config(font=("Arial", 24))

        
            questionimg=self.RandomQ[0][0]
            print(self.RandomQ)
            print("############")
       #questionimg
            self.physicsquestion = tk.Canvas(self, width=1000, height=276, bg="white", borderwidth=0, highlightthickness=0)
            self.physicsquestionimg= tk.PhotoImage(file=questionimg)
            self.physicsquestion.create_image(0,0 ,image=self.physicsquestionimg, anchor="nw")
            self.physicsquestion.configure(background="white")
            self.physicsquestion.grid(row=1, column=2, columnspan=2, sticky="NSWE")


        #answerbox
            self.answerbox = tk.Entry(self,text="Enter Answer")
            self.answerbox.grid(row=8,column=2,sticky="NSEW")
        
        #question num text
      #  questionnumber=i
            self.questionnum = tk.Label(self, text="Q num")
            self.questionnum.grid(row=0, column=1, sticky="NSWE")
            self.questionnum.configure(background="white")
            self.questionnum.config(font=("Arial", 24))
        
        #hint button
        
            hintbuttonstatus=tk.DISABLED
           # print(hintbuttonstatus)
            self.hintbuttonimage= tk.PhotoImage(file="hintbutton.png")
            self.hintbutton=tk.Button(self, text="hint",command=self.hintpressed, state=hintbuttonstatus,image=self.hintbuttonimage)
            self.hintbutton.grid(row=2,column=4,columnspan=1,sticky="NSWE")

       #submit button
            self.submitbutton=tk.Button(self, text="submit",command=self.Answerpressed)
            self.submitbutton.grid(row=9,column=2,columnspan=1,sticky="NSWE")

            self.textcolor="Red"
            self.textcontents=""
        #question C/W label
            self.right_or_wrong = tk.Label(self, text=" ",fg=self.textcolor)
            self.right_or_wrong.grid(row=10, column=2, sticky="NSWE")
            self.right_or_wrong.configure(background="white")
            self.right_or_wrong.config(font=("Georgia", 24))
        else:

           
            self.ReviewProgress()
            
    def ReviewProgress(self):
        self.model_answer.grid_forget()
        self.correct_answer_label.grid_forget()
        self.tryagain.grid_forget()
        self.nextQ.grid_forget()
        
        print("##########final question array with waeighting")
        print(self.final_question_array_with_weighting)
        print("##########final question array with waeighting")

     #Test completed label
        self.Testcompleted = tk.Label(self, text="TestCompleted")
        self.Testcompleted.grid(row=1, column=2,columnspan=2 ,sticky="NSWE")
        self.Testcompleted.configure(background="white")
        self.Testcompleted.config(font=("Georgia", 24))

        #Score label
        self.Scorelbl = tk.Label(self, text="Score")
        self.Scorelbl.grid(row=3, column=2, sticky="NSWE")
        self.Scorelbl.configure(background="white")
        self.Scorelbl.config(font=("Georgia", 24))

        #QuestionsCorrect Topic label
        self.QuestionsCorrectlbl = tk.Label(self, text="Questions Correct: ")
        self.QuestionsCorrectlbl.grid(row=3, column=2, sticky="NSWE")
        self.QuestionsCorrectlbl.configure(background="white")
        self.QuestionsCorrectlbl.config(font=("Georgia", 24))

       

        #Best Topic label
        self.best_topic_label = tk.Label(self, text="Best Topic: ")
        self.best_topic_label.grid(row=4, column=2, sticky="NSWE")
        self.best_topic_label.configure(background="white")
        self.best_topic_label.config(font=("Georgia", 24))
        
        #Worst Topic label
        self.worst_topic = tk.Label(self, text="Worst Topic: ")
        self.worst_topic.grid(row=5, column=2, sticky="NSWE")
        self.worst_topic.configure(background="white")
        self.worst_topic.config(font=("Georgia", 24))


        self.QuestionsCorrectNum = tk.Label(self, text=" ")
        self.QuestionsCorrectNum.grid(row=1, column=1, sticky="NSWE")
        self.QuestionsCorrectNum.configure(background="white")
        self.QuestionsCorrectNum.config(font=("Georgia", 24))


        #QuestionsCorrect actual number Topic label
        
        self.QuestionsCorrectNum = tk.Label(self, text=str(self.QuestionsCorrect) +"/10")
        self.QuestionsCorrectNum.grid(row=3, column=3, sticky="NSWE")
        self.QuestionsCorrectNum.configure(background="white")
        self.QuestionsCorrectNum.config(font=("Georgia", 24))

       

        #Best Topic label number
        self.best_topic_labelnum = tk.Label(self, text="" )
        self.best_topic_labelnum.grid(row=4, column=3, sticky="NSWE")
        self.best_topic_labelnum.configure(background="white")
        self.best_topic_labelnum.config(font=("Georgia", 24))
        

        #Worst Topic label
        self.worst_topicnum = tk.Label(self, text=" ")
        self.worst_topicnum.grid(row=5, column=3, sticky="NSWE")
        self.worst_topicnum.configure(background="white")
        self.worst_topicnum.config(font=("Georgia", 24))


        #continue button
        self.submitbutton=tk.Button(self, text="Continue",command=self.parent.switchtomainscreen)
        self.submitbutton.grid(row=6,column=2,columnspan=2,sticky="NSWE")
        




    

            









