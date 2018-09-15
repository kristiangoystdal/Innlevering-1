# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:32:54 2018

@author: krisg
"""
"""Importerer en tidspakke og en mattepakke for å kunne pause programmet og 
regne ut kompliserte mattelikninger"""
import math
import time

"""Lagde en while løkke som spør om hva du vil regne ut av masse, energi og fart
og kjører den til du velger en av de 3"""
while True:
    variabel=input("Hvilken vil du regne ut energi(E), masse(m) eller fart(v)?   ")
    
    if variabel == "E" or variabel == "m" or variabel == "v":
        print("")
        print("")
        print("")
        time.sleep(2)
        break
    else: 
        print("")
        print("")
        time.sleep(2)
        print("Dette er en variabel som ikke kan regnes ut... Velg noe annet...   ")
        time.sleep(1)

"""Programmet ser etter hvilken variabel du valgte ut ifra inputen og kjører en 
if-setning basert på riktig variabel, hvor den da spør om de to andre variabelene
slik at den kan regne ut den variabelen du valgte"""

if variabel == "E":
    print("Du har valgt å regne ut energien til legeme...")
    print("")
    time.sleep(1)
    masse=float(input("Hva er massen til legeme? Oppgi i kg...   "))
    print("")
    time.sleep(1)
    fart=float(input("Hva er farten til legeme? Oppgi i m/s...   "))
    time.sleep(2)
    
    print("")
    print("")
    print("..........REGNER UT ENERGI..........")
    print("")
    print("")
    
    svar= (1/2)*masse*(fart**2)
    time.sleep(3)

    print("Den kinetiske energien er", svar, "J")
    
elif variabel == "m":
    print("Du har valgt å regne ut massen til legeme...")
    print("")
    time.sleep(1)
    energi=float(input("Hvor mye energi har legeme? Oppgi i J...   "))
    print("")
    time.sleep(1)
    fart=float(input("Hva er farten til legeme? Oppgi i m/s...   "))
    time.sleep(2)
    
    print("")
    print("")
    print("..........REGNER UT MASSEN..........")
    print("")
    print("")
    
    svar= 2*(energi/(fart**2))
    time.sleep(3)

    print("Massen er", svar, "kg")
    
else:
    print("Du har valgt å regne ut farten til legeme...")
    print("")
    time.sleep(1)
    energi=float(input("Hvor mye energi har legeme? Oppgi i J...   "))
    print("")
    time.sleep(1)
    masse=float(input("Hva er massen til legeme? Oppgi i kg...   "))
    time.sleep(2)
    
    print("")
    print("")
    print("..........REGNER UT FARTEN..........")
    print("")
    print("")
    
    svar= math.sqrt(2*(energi/masse))
    time.sleep(3)

    print("Farten er", svar, "m/s")




