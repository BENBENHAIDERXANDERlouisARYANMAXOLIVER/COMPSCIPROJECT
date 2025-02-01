import tkinter as tk

class SettingsFrame(tk.Frame):
    
    def __init__(self, parent):
        self.parent = parent
        self.faker=1
        self.prohibitedtopics=[]
        self.db = parent.db
        tk.Frame.__init__(self, parent)
        self.configure(background="white")
        self.parent.bind("<Return>")


        #settings label
        self.settings_label = tk.Label(self, text="Settings")
        self.settings_label.grid(row=0, column=2, columnspan=1, sticky="NSWE")
        self.settings_label.configure(background="white")
        self.settings_label.config(font=("Arial", 48))
        
        #lil cog canvas
        self.cogLabel = tk.Canvas(self, width=10, height=10, bg="white", borderwidth=0, highlightthickness=0)
        self.cogimage= tk.PhotoImage(file="COG.png")
        self.cogLabel.create_image(0,0 ,image=self.cogimage, anchor="nw")
        self.cogLabel.configure(background="white")
        self.cogLabel.grid(row=0, column=1, columnspan=1, sticky="NESW")
        self.columnconfigure(1,minsize=50)
     
     #back button
       # self.backbutton= tk.PhotoImage(file="hintbutton.png")
        self.backbutton=tk.Button(self, relief="groove",command=self.parent.switchtomainscreen,text="Back to Main Screen")
        self.backbutton.grid(row=0,column=0,sticky="NSWE")
        

       #toggle topics text
        self.toggle_topic_lbl = tk.Label(self, text="Toggle Topic :")
        self.toggle_topic_lbl.grid(row=1, column=0, columnspan=3, sticky="NSWE")
        self.toggle_topic_lbl.configure(background="white")
        self.toggle_topic_lbl.config(font=("Arial", 24)) 
    
        #Magnetism toggle text
        self.magnetism_toggle_text = tk.Label(self, text="Magnetism")
        self.magnetism_toggle_text.grid(row=2, column=0, sticky="NSWE")
        self.magnetism_toggle_text.configure(background="white")
        self.magnetism_toggle_text.config(font=("Arial", 12))

        self.checked_magnetism = tk.IntVar(value=1)
        
        self.mag_toggle = tk.Checkbutton(self,variable=self.checked_magnetism ,indicatoron=1)
        self.mag_toggle.grid(row=2, column=1, sticky="NSWE")
        self.mag_toggle.configure(background="white")
        self.mag_toggle.config(font=("Arial", 12))



        #Nuclear toggle t
        self.nuclear_toggle_text = tk.Label(self, text="Nuclear")
        self.nuclear_toggle_text.grid(row=3, column=0, sticky="NSWE")
        self.nuclear_toggle_text.configure(background="white")
        self.nuclear_toggle_text.config(font=("Arial", 12))

        self.checked_nuclear = tk.IntVar(value=1)
        self.nuclear_toggle = tk.Checkbutton(self,variable=self.checked_nuclear ,indicatoron=1)
        self.nuclear_toggle.grid(row=3, column=1, sticky="NSWE")
        self.nuclear_toggle.configure(background="white")
        self.nuclear_toggle.config(font=("Arial", 12)) 

        #fmechanics toggle text
        self.fmechanics_toggle_text = tk.Label(self, text="F mechanics")
        self.fmechanics_toggle_text.grid(row=4, column=0, sticky="NSWE")
        self.fmechanics_toggle_text.configure(background="white")
        self.fmechanics_toggle_text.config(font=("Arial", 12))
        
        self.checked_fmechanics = tk.IntVar(value=1)
        self.fmechanics_toggle = tk.Checkbutton(self,variable=self.checked_fmechanics ,indicatoron=1)
        self.fmechanics_toggle.grid(row=4, column=1, sticky="NSWE")
        self.fmechanics_toggle.configure(background="white")
        self.fmechanics_toggle.config(font=("Arial", 12)) 

        #mechanics toggle text
        self.mechanics_toggle_text = tk.Label(self, text="Mechanics")
        self.mechanics_toggle_text.grid(row=5, column=0, sticky="NSWE")
        self.mechanics_toggle_text.configure(background="white")
        self.mechanics_toggle_text.config(font=("Arial", 12))

        self.checked_mechanics = tk.IntVar(value=1)
        self.mechanics_toggle = tk.Checkbutton(self,variable=self.checked_mechanics ,indicatoron=1)
        self.mechanics_toggle.grid(row=5, column=1, sticky="NSWE")
        self.mechanics_toggle.configure(background="white")
        self.mechanics_toggle.config(font=("Arial", 12)) 


       #Particles toggle text
        self.particles_toggle_text = tk.Label(self, text="Particles")
        self.particles_toggle_text.grid(row=2, column=2, sticky="NSWE")
        self.particles_toggle_text.configure(background="white")
        self.particles_toggle_text.config(font=("Arial", 12))

        self.checked_particles = tk.IntVar(value=1)
        self.particles_toggle = tk.Checkbutton(self,variable=self.checked_particles ,indicatoron=1)
        self.particles_toggle.grid(row=2, column=3, sticky="NSWE")
        self.particles_toggle.configure(background="white")
        self.particles_toggle.config(font=("Arial", 12)) 
       
       
       
       # Quantum 
        self.Quantum_toggle_text = tk.Label(self, text="Quantum")
        self.Quantum_toggle_text.grid(row=3, column=2, sticky="NSWE")
        self.Quantum_toggle_text.configure(background="white")
        self.Quantum_toggle_text.config(font=("Arial", 12))

        self.checked_Quantum = tk.IntVar(value=1)
        self.Quantum_toggle = tk.Checkbutton(self,variable=self.checked_Quantum ,indicatoron=1)
        self.Quantum_toggle.grid(row=3, column=3, sticky="NSWE")
        self.Quantum_toggle.configure(background="white")
        self.Quantum_toggle.config(font=("Arial", 12)) 
       
       
       
        # Waves/optics 
        self.W_And_O_toggle_text = tk.Label(self, text="Waves/optics")
        self.W_And_O_toggle_text.grid(row=2, column=6, sticky="NSWE")
        self.W_And_O_toggle_text.configure(background="white")
        self.W_And_O_toggle_text.config(font=("Arial", 12))

        self.checked_W_And_O = tk.IntVar(value=1)
        self.W_And_O_toggle = tk.Checkbutton(self,variable=self.checked_W_And_O ,indicatoron=1)
        self.W_And_O_toggle.grid(row=2, column=7, sticky="NSWE")
        self.W_And_O_toggle.configure(background="white")
        self.W_And_O_toggle.config(font=("Arial", 12))

        #materials
        self.materials_toggle_text = tk.Label(self, text="materials")
        self.materials_toggle_text.grid(row=4, column=2, sticky="NSWE")
        self.materials_toggle_text.configure(background="white")
        self.materials_toggle_text.config(font=("Arial", 12))

        self.checked_materials = tk.IntVar(value=1)
        self.materials_toggle = tk.Checkbutton(self,variable=self.checked_materials ,indicatoron=1)
        self.materials_toggle.grid(row=4, column=3, sticky="NSWE")
        self.materials_toggle.configure(background="white")
        self.materials_toggle.config(font=("Arial", 12))



        #electricity
        self.electricity_toggle_text = tk.Label(self, text="electricity")
        self.electricity_toggle_text.grid(row=5, column=2, sticky="NSWE")
        self.electricity_toggle_text.configure(background="white")
        self.electricity_toggle_text.config(font=("Arial", 12))

        self.checked_electricity = tk.IntVar(value=1)
        self.electricity_toggle = tk.Checkbutton(self,variable=self.checked_electricity ,indicatoron=1)
        self.electricity_toggle.grid(row=5, column=3, sticky="NSWE")
        self.electricity_toggle.configure(background="white")
        self.electricity_toggle.config(font=("Arial", 12))
       
       
       
        #Astrophysics
        self.astro_toggle_text = tk.Label(self, text="Astrophysics")
        self.astro_toggle_text.grid(row=2, column=4, sticky="NSWE")
        self.astro_toggle_text.configure(background="white")
        self.astro_toggle_text.config(font=("Arial", 12))

        self.checked_astro = tk.IntVar(value=1)
        self.astro_toggle = tk.Checkbutton(self,variable=self.checked_astro ,indicatoron=1)
        self.astro_toggle.grid(row=2, column=5, sticky="NSWE")
        self.astro_toggle.configure(background="white")
        self.astro_toggle.config(font=("Arial", 12))
    
    
    
        #thermal
        self.thermal_toggle_text = tk.Label(self, text="thermal")
        self.thermal_toggle_text.grid(row=3, column=4, sticky="NSWE")
        self.thermal_toggle_text.configure(background="white")
        self.thermal_toggle_text.config(font=("Arial", 12))

        self.checked_thermal = tk.IntVar(value=1)
        self.thermal_toggle = tk.Checkbutton(self,variable=self.checked_thermal ,indicatoron=1)
        self.thermal_toggle.grid(row=3, column=5, sticky="NSWE")
        self.thermal_toggle.configure(background="white")
        self.thermal_toggle.config(font=("Arial", 12))
       
       
       
        #gravity
        self.gravity_toggle_text = tk.Label(self, text="gravity")
        self.gravity_toggle_text.grid(row=4, column=4, sticky="NSWE")
        self.gravity_toggle_text.configure(background="white")
        self.gravity_toggle_text.config(font=("Arial", 12))
        self.checked_gravity = tk.IntVar(value=1)
        
        self.gravity_toggle = tk.Checkbutton(self,variable=self.checked_gravity ,indicatoron=1)
        self.gravity_toggle.grid(row=4, column=5, sticky="NSWE")
        self.gravity_toggle.configure(background="white")
        self.gravity_toggle.config(font=("Arial", 12))
        
        
        
        #electric fields
        self.elecFields_toggle_text = tk.Label(self, text="Elec fields")
        self.elecFields_toggle_text.grid(row=5, column=4, sticky="NSWE")
        self.elecFields_toggle_text.configure(background="white")
        self.elecFields_toggle_text.config(font=("Arial", 12))
       
        self.checked_elecFields = tk.IntVar(value=1)
        self.elecFields_toggle = tk.Checkbutton(self,variable=self.checked_elecFields ,indicatoron=1)
        self.elecFields_toggle.grid(row=5, column=5, sticky="NSWE")
        self.elecFields_toggle.configure(background="white")
        self.elecFields_toggle.config(font=("Arial", 12))
        
        self.topicList=[[self.checked_magnetism,"Magnetism"],[self.checked_elecFields,"electric fields"],[self.checked_gravity,"Gravity"],[self.checked_thermal,"thermal"],[self.checked_astro,"astrophysics"], [self.checked_electricity,"Electricity"], [self.checked_materials,"materials"],[self.checked_W_And_O,"Waves"],[self.checked_Quantum,"Quantum"],[self.checked_particles,"Particles"],[self.checked_mechanics,"Mechanics"], [self.checked_fmechanics,"Further Mechanics"], [self.checked_nuclear,"Nuclear"]]

     #submit options button
        self.submitoptions=tk.Button(self, text="Submit",bg="#5100FF",fg="white", font="Georgia", activebackground="#f1ed0e",relief="groove",command=self.checkboxchecker)
        self.submitoptions.grid(row=6,column=1,columnspan=3,sticky="NSWE") 
        
        
        #statistics page   button
        self.submitoptions=tk.Button(self, text="Stats",bg="#FFFF00",fg="black", font="Georgia", activebackground="#f1ed0e",relief="groove",command=self.parent.switchtostatsFrame)
        self.submitoptions.grid(row=7,column=7,columnspan=2,sticky="NSWE") 
        
        
         #delete account   button
        self.submitoptions=tk.Button(self, text="Delete Account",bg="red",fg="white", font="Georgia", activebackground="black",relief="groove",command=self.deleteaccount)
        self.submitoptions.grid(row=8,column=7,columnspan=2,sticky="NSWE") 

      
      
      
      
      #toggle hint text
        self.hint_toggle_text = tk.Label(self, text="hints on/off")
        self.hint_toggle_text.grid(row=7, column=0, sticky="NSWE")
        self.hint_toggle_text.configure(background="white")
        self.hint_toggle_text.config(font=("Arial", 12))
        
        self.checked_hint = tk.IntVar(value=1)
        
        self.hint_toggle = tk.Checkbutton(self,variable=self.checked_hint ,indicatoron=1,command=self.checkhinton)
        self.hint_toggle.grid(row=7, column=1, sticky="NSWE")
        self.hint_toggle.configure(background="white")
        self.hint_toggle.config(font=("Arial", 12))

        #toggle topics text
        self.topics_toggle_text = tk.Label(self, text="show topics on/off")
        self.topics_toggle_text.grid(row=7, column=2, sticky="NSWE")
        self.topics_toggle_text.configure(background="white")
        self.topics_toggle_text.config(font=("Arial", 12))
        
        self.checked_topics = tk.IntVar(value=1)
        
        self.topics_toggle = tk.Checkbutton(self,variable=self.checked_topics ,indicatoron=1,command=self.checktopicon)
        self.topics_toggle.grid(row=7, column=3, sticky="NSWE")
        self.topics_toggle.configure(background="white")
        self.topics_toggle.config(font=("Arial", 12))
  












  

    def magbuttonpressed(self):
        if(self.indicatoron==1):
            print("magnetism selected")
        if(self.indicatoron==0):
            print("magnetism not selected")


    def back_button_command(self):
        print("meepmeep")
        

    

    def loadUp(self):
        print("loaded Login")
        # print("Bypassed login")
        # self.controller.successfulLogin("asmith")
   
   #hint button toggle 
    def checkhinton(self):
        if self.checked_hint.get()==0:
            self.parent.hintstate=0
        

#check topic toggled
    def checktopicon(self):
        if self.checked_topics.get()==0:
            self.parent.topicbuttonstate=0
            print("checktopicworking")

    def movetostatspage(self):
        print("working and ready for future implementation")

    def deleteaccount(self):
        self.parent.switchtodeleteFrame()
        #is being accessed

    
    def checkboxchecker(self):
        for item in self.topicList:
            checked=item[0].get()
            
            if(checked==0):
                self.parent.prohibitedtopics.append(item[1])
            
                

           


          #  getter=str(item[1])
            #print("THIS IS THE GETTER"+ getter)
          #  howlong=len(getter)
           # if howlong>=8:
         #       print(item)
          #  else:
          #      print(getter)
          #      print(getter[6])
          #      if(item[0].get==0):
           #         self.prohibitedtopics.append(item[0])
           #         print("item disallowed")
           #     else:
           #         print("item allowed")
                
            
