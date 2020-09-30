#UI Creation to display what si calculated in hipanalysis.py

from tkinter import * 
import sys
import hipanalysis #Functions defined in hipanalysis are called
import math

#Creates Window class that inherits from the Frame class
class Window(Frame):
#Defines the settings of the master widget upon initialization 
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Hip Implant Calculations")
        self.pack(fill = BOTH, expand = 1)

        #Labels displayed on the UI 

        #Creates Label
        titleLabel = Label(self, text = "Team 15: Hip Implant Calculator")
        #Places Label on UI canvas
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        #Configures the label
        titleLabel.configure(font="TkDefaultFont 18")

        baseMeasurements = Label(self, text = "Base Measurements")
        baseMeasurements.place(relx = 0.05, rely = 0.14, anchor = W)
        baseMeasurements.configure(font = "TkDefaultFont 14")

        body_weight = 72*9.81
        bodyWeight = Label(text =("Body","Weight:", body_weight, "N"))
        bodyWeight.place(relx = 0.05, rely = 0.18, anchor = W)

        canal_diameter = 17
        canalDiameter = Label(text =("Canal","Diameter:", canal_diameter, "mm"))
        canalDiameter.place(relx = 0.25, rely = 0.18, anchor = W)

        ult_ten_strength = 1200
        ultTenStrength = Label(text = ("Ultimate","Tensile","Strength","of", "Ti-6Al-4V:", ult_ten_strength, "Mpa"))
        ultTenStrength.place(relx = 0.45, rely = 0.18, anchor = W)

        outer_diameter = 32
        outerDiameter = Label(text = ("Outer", "Diameter:", outer_diameter, "MM"))
        outerDiameter.place(relx = 0.75, rely = 0.18, anchor = W)
        
        canal_offset = 40
        canalOffset = Label(text = ("Canal", "Offset:", canal_offset, "MM"))
        canalOffset.place(relx = 0.05, rely = 0.24, anchor = W)

        modulus_bone = 17
        modulusBone = Label(text = ("Modulus", "Of", "Bone:", modulus_bone, "MPa"))
        modulusBone.place(relx = 0.25, rely = 0.24, anchor = W)

        modulus_implant = 114
        modulusImplant = Label(text = ("Modulus", "Of", "Implant:", modulus_implant, "MPa"))
        modulusImplant.place(relx = 0.45, rely = 0.24, anchor = W)

        stem_dia = 17
        stemDiameter = Label(text = ("Stem", "Diameter:", stem_dia, "MM"))
        stemDiameter.place(relx = 0.75, rely = 0.24, anchor = W)

        labelFunctions = Label(self, text = "Functions")
        labelFunctions.place(relx = 0.05, rely = 0.28, anchor = W)
        labelFunctions.configure(font = "TKdefaultFont 14")

        #Buttons displayed on UI. Each button runs functions defined in hipanalysis

        #Creates Button, command references functions in hipanalysis
        func1Button = Button(self, text = "Minimum Stem Diameter", command = hipanalysis.textSubProgram1)
        #Places Button on UI canvas
        func1Button.place(relx = 0.05, rely = 0.32, anchor = W)
        #Configures Button
        func1Button.configure(height = 2, width = 50)

        func2Button = Button(self, text = "Function 2", command = hipanalysis.textSubProgram2)
        func2Button.place(relx = 0.05, rely = 0.50, anchor = W)
        func2Button.configure(height = 2, width = 50)

        func3Button = Button(self, text = "Function 3", command = hipanalysis.textSubProgram3)
        func3Button.place(relx = 0.55, rely = 0.315, anchor = W)
        func3Button.configure(height = 2, width = 50)

        quitButton = Button(self, text = "QUIT", fg = "red", command = self.master.destroy)
        quitButton.place(relx = 0.5, rely = 0.95, anchor = CENTER)
        quitButton.configure(height = 2, width = 30)

#Creates root window
root = Tk()
root.geometry("1000x1000")
#Creates an instance 
app = Window(root)
#Creates an infinite loop that runs the root window 
root.mainloop()
