#Program that calculates various properties of a hip implant then sends data to UI 
#All functions have been written by myself unless specified 

import math
from tkinter import *
import sys

team_number = 15
body_weight = float(72*9.81)
outer_dia = 32
canal_diameter = 17
canal_offset = 40
modulus_bone = 17 
modulus_implant = 114 
stem_dia = 17

#Subprogram 1: calculating minimum stem diameter
def subProgram1():
    app_ten_stress = 0
    d = stem_dia
    values = [] #Used to print diameter and tensile strenght to the UI
    
    #itterate applied tensile stress and diameter until it equals 1200 (ultimate tensile strength)
    while round(app_ten_stress) != 1200:
        app_ten_stress = round((79107840 - 247212*d)/(25*math.pi*d**3)) #applied tensile stress formula found in the book 
        if app_ten_stress == 1200:
            dia = round(d,2)
            stress = round(app_ten_stress, )
            return dia, stress
            break
        d = d-0.01

#Displays values calculated in subprogram1 - Called by the UI
def textSubProgram1():
    dia, stress = subProgram1()
    
    #Creates and places label on UI canvas  
    diameter = Label(text = ("Minimum", "Diameter:", dia, "mm"))
    diameter.place(relx = 0.07, rely = 0.38, anchor = W)

    appTenStress = Label(text = ("Applied", "Tensile", "Stress", "For", "Minimum", "Diameter:", stress, "MPa"))
    appTenStress.place(relx = 0.07, rely = 0.42, anchor = W)

#Subprogram2: Calculates Fatigue Life (team member wrote this function)
def subProgram2(): 
    r = []
    area = math.pow(stem_dia,2)* math.pi/4 #Cross-sectional area of the femoral stem
    max_load = 10*body_weight
    min_load = -10*body_weight
    max_stress = (max_load/area)
    min_stress = (min_load/area)

    ##calculating stress amplitude
    stress_amp = round((max_stress - min_stress)/2)
    
    ##dividing the columns (assosiated with Stress and cycles to fail in the file respectively) and putting the values in each column into lists and making each value a float
    S = []
    N = []
    
    SN_file = open("SN Data - Sample Metal.txt", 'r')
    for line in SN_file:
        data = line.split()
        S.append(float(data[0]))
        N.append(float(data[1])) 
    SN_file.close()
    
    ## for each value in the cycles to fail list (N) we calculate a new Kn (stress cncentration) 
    for value in N:
        cycles_to_failure = value
        Kn = round(6 + math.pow(math.log10(cycles_to_failure),(team_number/30)),2)

    ##calculating the adjusted-stress amplitude by multiplying the stress amplitude calculated in the begining by Kn (which changes according to values in N)
    Stress_amp_adj = round(Kn * stress_amp)
    
    r.append(Stress_amp_adj)

    ##as the adjusted stress amplitude is still not within the list of S we use this while loop to increase the vlue of adjusted stress amplited to get the a value within the list to get a corrisponding value of cycles to failure (the greatest value)
    while Stress_amp_adj not in S:       
        Stress_amp_adj += 1
        
    cycles = N[S.index(Stress_amp_adj)]    

    r.append(int(N[-1]))
    return r

#Displays values calculated by subprogram2 - Called by UI
def textSubProgram2():
    values = subProgram2()
    stress_amp_adj = values[0]
    N = values[1]

    #Creates and places labels on UI canvas 
    stressAmp = Label(text = ("Adjusted", "Stress", "Amplitude:", stress_amp_adj, "MPa"))
    stressAmp.place(relx = 0.13, rely = 0.56, anchor = W)

    cycles = Label(text = ("Cyles", "To", "Failure", "Is", "Greater", "Than:", N))
    cycles.place(relx = 0.13, rely = 0.6, anchor = W)

#Subprogram3: Calculates years until failure (Team member wrote this function)
def subprogram3():
    axial_comp_load = 30*body_weight
    area_bone = (math.pi/4*(math.pow(outer_dia,2)-math.pow(canal_diameter,2)))
    comp_stress_bone = (axial_comp_load)/(area_bone)  
    stress_reduc = comp_stress_bone * math.sqrt((2*modulus_bone)/(modulus_bone + modulus_implant))
    E_ratio = math.sqrt((modulus_implant)/(modulus_bone))

    y = []
    cs = []
    years_fail = 0 #x is the number of years

    ##using a while loop to see if the compressive strength is greater than the stress reduction and adding 1 if its true
    while(True):
        comp_strength = (0.001 * (years_fail**2)) - (3.437 * years_fail * E_ratio) + 181.72
        if comp_strength >= stress_reduc:
            years_fail += 1
            y.append(years_fail)
            cs.append(comp_strength)
        else:
            break

    return y, cs

#Displays values calculated in subprogram3 - Called by UI
def textSubProgram3():
    y, cs = subprogram3()
    cs = [round(x) for x in cs]

    #Variables used to place labels 
    x = 0.355
    g = 0.355
    h = 0.355

    #Create label and place on UI canvas 
    year1 = Label(text = ("Year:"))
    year1.place(relx = 0.55, rely = 0.36, anchor = W)

    #Creates and places a label on the UI canvas for all values stored in y array
    for i in range(y[0],y[14]):    
        year = Label(text = (i))
        year.configure(text = (i))
        year.place(relx = 0.559, rely = (i+10.5)*0.035, anchor = W)
    
    compStrength1 = Label(text = ("Comp Strength MPa:"))
    compStrength1.place(relx = 0.6, rely = 0.36, anchor = W)

    for z in range(y[13],y[-1]):
        h += 0.042
        year = Label(text = (z+1))
        year.configure(text = (z+1))
        year.place(relx = 0.75, rely = h, anchor = W)
   
    #Creates and placing labels on UI canvas 
    year2 = Label(text = ("Year:"))
    year2.place(relx = 0.745, rely = 0.36, anchor = W)

    compStrength2 = Label(text = ("Comp Strength MPa:"))
    compStrength2.place(relx = 0.79, rely = 0.36, anchor = W)

    #Creates and places a label on UI canvas for all values stored in cs array 
    for n in cs:
        if(n >= cs[13]):
            x += 0.03663
            strength = Label(text = (n))
            strength.configure(text = (n))
            strength.place(relx = 0.65, rely = x, anchor = W)
        elif(n <=cs[13]):
            g += 0.042
            st = Label(text = (n))
            st.configure(text = (n))
            st.place(relx = 0.8355, rely = g, anchor = W)

    failLabel = Label(text = ("Implant", "fails", "at", y[-1], "years", ",compressive", "strength", "is", cs[-1], "MPa"))
    failLabel.place(relx = 0.685, rely = 0.65, anchor = W)
