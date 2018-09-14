# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:32:54 2018

@author: krisg
"""

import math
import time

while True:
    grunntall=int(input("Hva er konsentrasjonen av H+ ioner? Oppgi bare grunntallet, eks: 2,1...   "))
    
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

verdi=(math.log10((grunntall*(10**grad))))*-1
verdi = round(verdi,2)

if 0 <= verdi < 7:
    pH = "SUR"
elif verdi == 7:
    pH = "NØYTRAL"
else:
    pH = "BASISK"

print("")
print("")
print("Din pH-verdi er", verdi, "og løsningen er", pH)
