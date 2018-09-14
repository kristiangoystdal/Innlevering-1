# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:56:54 2018

@author: krisg
"""

import time

while True:
    dyr = int(input("Hvor mange dyr er det?   "))
    
    print("")
    print("")
    time.sleep(2)
    
    if dyr > 0:
        prosent = float(input("Hvor mange prosent stiger eller synker bestanden med per år? Oppgi stigning positivt og senkelse negativ...   " ))
        
        print("")
        print("")
        time.sleep(2)

        år = int(input("Over hvor mange år foregår undersøkelsen?   "))
        print("")
        print("")
        time.sleep(2)
            
        if år > 0:
            break
        else:
            print("Det må være et tidsrom for undersøkelsen...")
    else:
        print("Man kan ikke starte med et negativt antall dyr...")

print("")
print("")
print("..........REGNER UT POULASJON ETTER TIDSROMMET..........")
print("")
print("")

for x in range(0, (år)):
    dyr=dyr*(1+(prosent/100))

dyr=round(dyr,0)
print("Antall dyr i bestanden etter", år, "år, er", dyr)
        
    
            
            
            
            
            
            
            
            