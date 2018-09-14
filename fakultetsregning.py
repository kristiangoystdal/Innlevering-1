# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:12:41 2018

@author: krisg
"""

import time

svar=1

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

tall = n
if n == 0:
    svar = 1.0
    
while tall > 0:
    svar *= tall
    tall-=1
    
print("Fakuleten til", n, "er", svar)