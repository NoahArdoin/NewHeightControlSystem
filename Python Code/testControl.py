# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 15:22:39 2023

@author: NoahA
"""

import serial
import tkinter as tk

s = serial.Serial()
s.baudrate = 9600
s.port = 'COM3'
if s.is_open :
    print('open')
else:
    s.open()

print(s)

# i = input("send command?")
# if i == 'y':
#     s.write(b'(1, U, 1)')
    