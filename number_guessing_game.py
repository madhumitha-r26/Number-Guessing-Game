# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:57:21 2025

@author: Madhumitha
"""

import random as rd

score=0
turns=int(input("ENTER NUMBER OF TIMES YOU WANT TO PLAY:"))
lower=int(input("ENTER LOWER LIMIT:"))
upper=int(input("ENTER UPPER LIMIT:"))

for i in range(1,turns):

    choice=int(input("ENTER YOUR CHOICE:"))
    
    random_number=rd.randint(lower,upper)
    
    
    if(random_number==choice):
        score+=1
        print("FANTASTIC!")
        
    else:
        if(score>0):
            score-=1
        print("THE NUMBER IS:",random_number)
        print("TRY AGAIN!")

print("YOUR SCORE=",score)
if(score==turns):
    print("YOU WON!")  
else:
    print("WELL PLAYED!")
