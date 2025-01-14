import tkinter as tk
from datetime import datetime,timedelta
from collections import defaultdict
class StatsFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>")
        self.Particlesscore=0
        self.Wavesscore=0
        self.Gravityscore=0
        self.Magnetismscore=0
        self.Electricityscore=0
        self.Mechanicsscore=0
        self.FurtherMechanicsscore=0
        self.Nuclearscore=0
        self.ListofArrays=[self.Particlesscore,self.Wavesscore,self.Gravityscore,self.Magnetismscore,self.Electricityscore,self.Mechanicsscore,self.FurtherMechanicsscore,self.Nuclearscore]
        self.ElectricityscoreTest=0
    
    def loadUp(self):
        
 
        #back button
       # self.backbutton= tk.PhotoImage(file="hintbutton.png")
        self.backbutton=tk.Button(self, relief="groove",command=self.parent.switchtosettings,text="Back to Settings")
        self.backbutton.grid(row=0,column=0,sticky="NSWE")

        #Statistic label
        statisticlabel = tk.Label(self, text="Statistics")
        statisticlabel.grid(row=0 ,column=1, columnspan=2, sticky="NSWE")
        statisticlabel.configure(background="white")
        statisticlabel.config(font=("Arial", 24))
        
        #graph and canvas
        self.theCanvas=tk.Canvas(self,width=800,height=450,bg="lightblue")
        self.theCanvas.grid(row=6,column=6,sticky="NSWE")


    #def plotGraph(self):
        c = self.db.cursor()
        r = c.execute("SELECT userid FROM tbluserdetails WHERE firstname = ?  ", [self.parent.loggedInUser])
        Founduserid=r.fetchone()
        a = c.execute("SELECT dateanswered,score FROM tbluserstats WHERE userid = ? ORDER BY dateanswered ASC ", [Founduserid[0]])
        Gdata=a.fetchall()
        print(Gdata)
        self.theCanvas.create_line(50,350,750,350,fill="black")
        self.theCanvas.create_line(50,50,50,350,fill="black")
        
        percent=0
        ycoord=360
        for i in range(10):
            percent =percent -10
            ycoord  -= 30
            splitpercent=str(percent)
            self.theCanvas.create_text(30,ycoord,text=str(splitpercent) +"%",anchor="center")



        graphData=defaultdict(list)
        for row in Gdata:

            
                day=row[0]
                daydate=day[:10]
                graphData[daydate].append(row[1])
        xpos=60
        for day in graphData:
            avgForDay= sum(graphData[day])/len(graphData[day])
            
           
            
            print(daydate,avgForDay)
            height=30000*avgForDay/100
           
            self.theCanvas.create_rectangle(xpos,350,xpos+20,350-height,fill="red")
            self.theCanvas.create_text(xpos+15,390,text=day,anchor="center",angle=90)
            self.theCanvas.create_text(400,15,text="AVERAGE PERCENTAGE BY DAY",anchor="center")
            
            xpos += 35

        
 




    ############## Best OVERALL TOPIC ############
           
        self.Electricityscore=self.parent.overall_topic_scoring(self.Electricityscore,"Electricity")
        self.Particlesscore=self.parent.overall_topic_scoring(self.Particlesscore,"Particles")
        self.Wavesscore=self.parent.overall_topic_scoring(self.Wavesscore,"Waves")
        self.Gravityscore=self.parent.overall_topic_scoring(self.Gravityscore,"Gravity")
        self.Magnetismscore=self.parent.overall_topic_scoring(self.Magnetismscore,"Magnetism")
        self.FurtherMechanicsscore=self.parent.overall_topic_scoring(self.FurtherMechanicsscore,"FurtherMechanics")
        self.Nuclearscore=self.parent.overall_topic_scoring(self.Nuclearscore,"Nuclear")
        self.Mechanicsscore=self.parent.overall_topic_scoring(self.Mechanicsscore,"Mechanics")
        
        self.ListofArrays=[self.Particlesscore,self.Wavesscore,self.Gravityscore,self.Magnetismscore,self.Electricityscore,self.Mechanicsscore,self.FurtherMechanicsscore,self.Nuclearscore]
        print(self.Particlesscore)
        print(self.Electricityscore)
        print(self.Wavesscore)
        print(self.Gravityscore)
        print(self.Magnetismscore)
        print(self.FurtherMechanicsscore)
        print(self.Mechanicsscore)
        print(self.Nuclearscore)
        scores = {
        "Particlesscore": self.Particlesscore,
        "Electricityscore": self.Electricityscore,
        "Wavesscore": self.Wavesscore,
        "Gravityscore": self.Gravityscore,
        "Magnetismscore": self.Magnetismscore,
        "FurtherMechanicsscore": self.FurtherMechanicsscore,
        "Mechanicsscore": self.Mechanicsscore,
        "Nuclearscore": self.Nuclearscore,}


        
        max_score_name = max(scores, key=scores.get)  
        
        BestTopic=max_score_name[:-5]
        min_score_name = min(scores, key=scores.get)
        WorstTopic=min_score_name[:-5]
        


        #weekly
        self.Electricityscore=self.parent.Weekly_topic_scoring(self.Electricityscore,"Electricity")
        self.Particlesscore=self.parent.Weekly_topic_scoring(self.Particlesscore,"Particles")
        self.Wavesscore=self.parent.Weekly_topic_scoring(self.Wavesscore,"Waves")
        self.Gravityscore=self.parent.Weekly_topic_scoring(self.Gravityscore,"Gravity")
        self.Magnetismscore=self.parent.Weekly_topic_scoring(self.Magnetismscore,"Magnetism")
        self.FurtherMechanicsscore=self.parent.Weekly_topic_scoring(self.FurtherMechanicsscore,"FurtherMechanics")
        self.Nuclearscore=self.parent.Weekly_topic_scoring(self.Nuclearscore,"Nuclear")
        self.Mechanicsscore=self.parent.Weekly_topic_scoring(self.Mechanicsscore,"Mechanics")
        
        self.ListofArrays=[self.Particlesscore,self.Wavesscore,self.Gravityscore,self.Magnetismscore,self.Electricityscore,self.Mechanicsscore,self.FurtherMechanicsscore,self.Nuclearscore]
        print(self.Particlesscore)
        print(self.Electricityscore)
        print(self.Wavesscore)
        print(self.Gravityscore)
        print(self.Magnetismscore)
        print(self.FurtherMechanicsscore)
        print(self.Mechanicsscore)
        print(self.Nuclearscore)
        scores = {
        "Particlesscore": self.Particlesscore,
        "Electricityscore": self.Electricityscore,
        "Wavesscore": self.Wavesscore,
        "Gravityscore": self.Gravityscore,
        "Magnetismscore": self.Magnetismscore,
        "FurtherMechanicsscore": self.FurtherMechanicsscore,
        "Mechanicsscore": self.Mechanicsscore,
        "Nuclearscore": self.Nuclearscore,}


        
        max_score_name = max(scores, key=scores.get)  
        
        BestTopicTW=max_score_name[:-5]
        min_score_name = min(scores, key=scores.get)
        WorstTopicTW=min_score_name[:-5]
        
        
        

        
            
                


           
                

        
        
        #Best overall topic label
        worstOtopiclbl = tk.Label(self, text="Best Topic (Overall):")
        worstOtopiclbl.grid(row=2 ,column=1, columnspan=2, sticky="NSWE")
        worstOtopiclbl.configure(background="white")
        worstOtopiclbl.config(font=("Arial", 24))

        #Best overall topic 
        worstOtopiclbl = tk.Label(self, text=BestTopic)
        worstOtopiclbl.grid(row=2 ,column=3, sticky="NSWE")
        worstOtopiclbl.configure(background="white")
        worstOtopiclbl.config(font=("Arial", 24))
      
       ############## Worst OVERALL TOPIC ############
       
        print(self.parent.overall_topic_scoring("Electricity",self.Electricityscore))
       
        #best overall topic label
        bestOtopiclbl = tk.Label(self, text="Worst Topic (Overall):")
        bestOtopiclbl.grid(row=1 ,column=1, columnspan=2, sticky="NSWE")
        bestOtopiclbl.configure(background="white")
        bestOtopiclbl.config(font=("Arial", 24))
        
        
        #best overall topic 
        bestOtopic = tk.Label(self, text=WorstTopic)
        bestOtopic.grid(row=1 ,column=3, sticky="NSWE")
        bestOtopic.configure(background="white")
        bestOtopic.config(font=("Arial", 24))


    ############## BEST TW TOPIC ############

        #best this week topic label
        bestTWtopiclbl = tk.Label(self, text="Best Topic (This Week):")
        bestTWtopiclbl.grid(row=4 ,column=1, columnspan=2, sticky="NSWE")
        bestTWtopiclbl.configure(background="white")
        bestTWtopiclbl.config(font=("Arial", 24))
       
        #best this week topic 
        bestTWtopic = tk.Label(self, text=BestTopicTW)
        bestTWtopic.grid(row=4 ,column=3, sticky="NSWE")
        bestTWtopic.configure(background="white")
        bestTWtopic.config(font=("Arial", 24))


    ############## Worst TW TOPIC ############


        #Worst This Week  topic label
        worstTWtopiclbl = tk.Label(self, text="Worst topic (This Week)")
        worstTWtopiclbl.grid(row=5 ,column=1, columnspan=2, sticky="NSWE")
        worstTWtopiclbl.configure(background="white")
        worstTWtopiclbl.config(font=("Arial", 24))
        
        #Worst This Week  topic 
        worstTWtopic = tk.Label(self, text=WorstTopicTW)
        worstTWtopic.grid(row=5 ,column=3, sticky="NSWE")
        worstTWtopic.configure(background="white")
        worstTWtopic.config(font=("Arial", 24))



        ############## Questions Answered ############
      
        c = self.parent.db.cursor()
        r = c.execute("SELECT userid FROM tbluserdetails WHERE firstname = ?  ", [self.parent.loggedInUser])
        Founduserid=r.fetchone()
        print(Founduserid)
        a = c.execute("SELECT * FROM tbluserstats WHERE userid = ?  ", [Founduserid[0]])
        Num_Of_Questions=a.fetchall()
        print(Num_Of_Questions)
        print("############################wf")
        noq=0
        for item in Num_Of_Questions:
            noq=noq+1


        #Questions Answered  topic label
        QAnsweredlbl = tk.Label(self, text="Questions Answered:")
        QAnsweredlbl.grid(row=1 ,column=4, columnspan=2, sticky="NSWE")
        QAnsweredlbl.configure(background="white")
        QAnsweredlbl.config(font=("Arial", 24))
        
        #Questions  Answered  topic 
        QAnswered = tk.Label(self, text=noq)
        QAnswered.grid(row=1 ,column=6, sticky="NSWE")
        QAnswered.configure(background="white")
        QAnswered.config(font=("Arial", 24))

        ############## Questions Correct ############
        TotalRight=0
        for item in Num_Of_Questions:
            if item[4]==1:
                TotalRight+=1



        #Questions Correct  topic label
        QCorrectlbl = tk.Label(self, text="Questions Correct:")
        QCorrectlbl.grid(row=2 ,column=4, columnspan=2, sticky="NSWE")
        QCorrectlbl.configure(background="white")
        QCorrectlbl.config(font=("Arial", 24))
        
        #Questions Correct  topic 
        QCorrect = tk.Label(self, text=TotalRight)
        QCorrect.grid(row=2 ,column=6, sticky="NSWE")
        QCorrect.configure(background="white")
        QCorrect.config(font=("Arial", 24))


        ############## overall % ############
        if noq !=0:

            Question_Percentage=(TotalRight/noq)*100
        else:
            Question_Percentage==0




        #Overall %  topic label
        OverallPercentagelbl = tk.Label(self, text="Questions %:")
        OverallPercentagelbl.grid(row=3 ,column=4, columnspan=2, sticky="NSWE")
        OverallPercentagelbl.configure(background="white")
        OverallPercentagelbl.config(font=("Arial", 24))
        
        #Questions Correct  topic 
        OverallPercentage = tk.Label(self, text=Question_Percentage)
        OverallPercentage.grid(row=3 ,column=6, sticky="NSWE")
        OverallPercentage.configure(background="white")
        OverallPercentage.config(font=("Arial", 24))
    


    


    

    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    