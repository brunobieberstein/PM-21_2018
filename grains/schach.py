#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:40:56 2018

@author: Bruno
"""

def feld_abfragen():
    while True:   
        a = input('Bitte ein Schachfeld angeben: ')
        try: 
            n = int(a)
        except(ValueError):
            print('Bitte eine Zahl zwischen 1 und 64 eingeben.')
            continue
        if n in range(1,65):
            break
        else:
            print('Bitte eine Zahl zwischen 1 und 64 eingeben.')
            continue
    return n

def on_square(n):
    return 2**(n-1)

def total_after(n):
    m=0
    while n >= 1:
        m = m + on_square(n)
        n = n-1
    return m





#main

n = feld_abfragen()

print('-------------------------------------------------------------------------')
print('Sie haben Feld 11 gewählt. \n')
print('Auf dem 11. Feld liegen', on_square(n), 'Reiskörner.')
print('Bis zu diesem Feld liegen insgesamt', total_after(n), 'Reiskörner auf dem Schachbrett.')
    
    
