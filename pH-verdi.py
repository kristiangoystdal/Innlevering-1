# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:32:54 2018

@author: krisg
"""
"""Importerer en tidspakke og en mattepakke for å kunne pause programmet og 
regne ut ph ved hjelp av logaritmer"""
import math
import time

"""Kjører en while løkke hvor den spør om et grunntall mellom 0 og 10 som 
definerer konsentrajonen til H+ ioner og deretter spør om i hvilken grad 
10 er opphøyd i, ved denne konsentrasjonen, mellom -14 til 0"""
while True:
    grunntall=float(input("Hva er konsentrasjonen av H+ ioner? Oppgi bare grunntallet, eks: 2,1...   "))
    
    print("")
    print("")
    
    if 0 < grunntall < 10:
        time.sleep(2)
        grad=int(input("Hvilken grad av 10 er konsentrasjonen i? eks: -3...   "))
        
        print("")
        print("")
        
        
        if -14 <= grad < 0:
            time.sleep(3)
            print("")
            print("")
            print("..........REGNER UT PH-VERDI..........")
            break
        else:
            time.sleep(2)
            print("Denne graden funker ikke...")
    else:
        
        time.sleep(1)
        print("Dette grunntallet kan ikke brukes...")

print("")
print("")
print("")
time.sleep(3)

"""Så regner den ut ph ved å hente inn en logaritme funksjon fra mattepakken og 
tar grunntall gange 10 opphøyd i den graden du oppga, og så runder den ph til 3 
desimaler"""
verdi=(math.log10((grunntall*(10**grad))))*-1
verdi = round(verdi,3)

"""Til slutt sjekker den om ph er under, lik eller over 7 og forteller om 
løsningen er sur, basisk eller nøytral"""
if 0 <= verdi < 7:
    pH = "SUR"
elif verdi == 7:
    pH = "NØYTRAL"
else:
    pH = "BASISK"

print("")
print("")
print("Din pH-verdi er", verdi, "og løsningen er", pH)
