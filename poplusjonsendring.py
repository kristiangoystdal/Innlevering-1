# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:56:54 2018

@author: krisg
"""
"""Importer en tidspakke som gjør at man kan lage pauser i programmene"""
import time

"""En while løkke som spør hvor mange dyr du har, hvor kun et positivt antall dyr 
funker, og så spør den om hvor mye bestanden stiger eller synker i prosent hvert 
år og en while løkke som spør om hvor mange år du undersøker, der man ikke 
kan skrive inn et negativt antall år"""
while True:
    dyr = int(input("Hvor mange dyr har du?   "))
    
    print("")
    print("")
    time.sleep(2)
    
    if dyr > 0:
        prosent = float(input("Hvor mange prosent stiger eller synker bestanden med per år? Oppgi stigning positivt og senkelse negativ...   " ))
        
        print("")
        print("")
        time.sleep(2)
        
        while True:
            år = int(input("Over hvor mange år foregår undersøkelsen?   "))
            print("")
            print("")
            time.sleep(2)
            
            if år >= 0:
                break
            else:
                print("Det må være et tidsrom for undersøkelsen...")
            break
    else:
        print("Man kan ikke starte med et negativt antall dyr...")

print("")
print("")
print("..........REGNER UT POULASJON ETTER TIDSROMMET..........")
print("")
print("")


"""Regner så ut antall dyr med å ta antall dyr og gange med den prosentvise 
økningen/senkelesen og sette det som et nytt antall og så gjør den det så mange 
år du valgte som undersøkelsesperioden"""
for x in range(0, (år)):
    dyr=dyr*(1+(prosent/100))

"""Runder antallet til nærmeste heltall, ettersom dyr ikke kommer i desimaltall"""
dyr=round(dyr,0)
print("Antall dyr i bestanden etter", år, "år, er", dyr)
        
    
            
            
            
            
            
            
            
            