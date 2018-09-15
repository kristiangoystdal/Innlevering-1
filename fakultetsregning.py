# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:12:41 2018

@author: krisg
"""

"Importerer en tidspakke sånn at jeg kan legge inn pauser i programmet"
import time

svar=1

"""Lagde en while løkke som spør om et tall du vil fakultere, men hvis du skriver
et negativt tall eller et tall med desimaler, får du beskjed om at det tallet
ikke funker og blir spurt på nytt"""

while True:
    n=float(input("Hvilket tall vil du fakultere?   "))
    
    if n >= 0 and n%1 == 0:
        break
    else:
        print("")
        time.sleep(2)
        print("Du kan kun fakultere et heltall eller et positivt tall...")
        time.sleep(1)

print("")
print("")
print("..........REGNER DU FAKULTET..........")
print("")
print("")
time.sleep(3)

"""Hvis tallet du skal fakultere er 0 vil den printe ut 1 som svar, og hvis ikke
vil den regne ut svaret ved å ta og gange tallet med 1 for å så trekke fra 1 og 
gange det med svaret fra forrige gjennomgang, altså tallet er 5, ganger 5 med 1 
og så ganger det svaret med 5-1 og så videre helt til til tallet man skal gange
med er 0"""
tall = n
if n == 0:
    svar = 1.0
    
while tall > 0:
    svar *= tall
    tall-=1
    
print("Fakuleten til", n, "er", svar)