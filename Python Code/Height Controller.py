# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:57:59 2023

@author: NoahA
"""

#%% Import Dependencies
from tkinter import *
from tkinter import ttk
import serial

#%% Global Variables
serialConnection = serial.Serial()  # stores the serial connection to arduino
heightTrackerA = 0.0                # stores the current height difference for A
heightTrackerB = 0.0                # stores the current height difference for B

#%% Functions
def connectArduino():
    # ---Function Description---
    # Establishes a serial connection to the arduino board 
    # with the specified port and baudrate. Saves connection
    # to a global variable.

    # Inputs:
    # comPort  : String : stores the COM port that the arduino is connected to
    # baudrate : int    : stores the baudrate of the serial connection (9600)

    # Set arguments
    comPort = 'COM3'
    baudrate = 9600

    # Use pyserial library to open serial connection
    serialConnection.baudrate = baudrate
    serialConnection.port = comPort

    # Check to there is not already a serial connection to arduino
    if serialConnection.is_open:
        print("A serial connection to arduino from a previous session is still open. Please restart kernel and arduino.")
    
    # Open serial connection
    serialConnection.open()

def sendCommand(heightChange, motorID):
    # ---Function Description---
    # Sends command over serial connection to arduino to control stepper motors
    
    # Inputs:
    # heightChange : float  : contains the desired height change and direction
    # motorID      : string : contains the id of the motor the command needs to be sent to

    # determine rotation direction
    if heightChange > 0:
        direction = 'U'
    else:
        direction = 'D'

    # determine number of rotations
    rotations = abs(heightChange) / 0.025

    # write command string
    command = '(' + motorID + ', ' + direction + ', ' + str(rotations) + ')'

    # send command to arduino
    serialConnection.write(command.encode())

def sendCommandA():
    # --- Function Description ---
    # runs when the "send command" button for motor A is pressed
    # executes the 'sendCommand' function with the proper arguments to send correct command to arduino
    
    # reference global variables
    global heightTrackerA
    
    # set arguments
    heightChange = float(spinval_A.get())
    motorID = '2'
    # execute sendCommand function
    sendCommand(heightChange, motorID)

    # update height tracker for A
    heightTrackerA += heightChange
    currentHeightA.set(f"{heightTrackerA:.2f}")
    
def sendCommandB():
    # --- Function Description ---
    # runs when the "send command" button for motor B is pressed
    # executes the 'sendCommand' function with the proper arguments to send correct command to arduino
    
    # reference global variables
    global heightTrackerB
    
    # set arguments
    heightChange = float(spinval_B.get())
    motorID = '1'
    # execute sendCommand function
    sendCommand(heightChange, motorID)

    # update height tracker for B
    heightTrackerB += heightChange
    currentHeightB.set(f"{heightTrackerB:.2f}")

def zeroA():
    # --- Function Description ---
    # Runs when the "Zero A" button is pressed
    # Resets the height tracker for motor A to zero, does not send commands to arduino
    
    global heightTrackerA
    
    heightTrackerA = 0
    currentHeightA.set(f"{heightTrackerA:.2f}")
    
def zeroB():
    # --- Function Description ---
    # Runs when the "Zero B" button is pressed
    # Resets the height tracker for motor B to zero, does not send commands to arduino
    
    global heightTrackerB
    
    heightTrackerB = 0
    currentHeightB.set(f"{heightTrackerB:.2f}")

#%% Body
#%%% Create GUI
root = Tk()
root.title("Motor Control")

# Create frame to attach UI elements to
mainframe = ttk.Frame(root, padding="4 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#%%% UI Elements
# connect arduino button
ttk.Button(mainframe, text="Connect Arduino", command=connectArduino).grid(column=1, row=1)

# text labels
ttk.Label(mainframe, text="Motor ID").grid(column=1, row=2, sticky=S)
ttk.Label(mainframe, text="Current Height Difference (in)").grid(column=2, row=2)
ttk.Label(mainframe, text="Height Increase/Decrease (in)").grid(column=3, row=2)
ttk.Label(mainframe, text="A").grid(column=1, row=3)
ttk.Label(mainframe, text="B").grid(column=1, row=4)

# height increase/decrease Spinboxes
spinval_A = DoubleVar()
ttk.Spinbox(mainframe, from_= -100.0, to= 100.0, textvariable = spinval_A, increment = 0.1).grid(column=3, row=3)
spinval_B = DoubleVar()
ttk.Spinbox(mainframe, from_= -100.0, to= 100.0, textvariable = spinval_B, increment = 0.1).grid(column=3, row=4)

#Height Difference trackers
currentHeightA = StringVar()
currentHeightLabelA = ttk.Label(mainframe, textvariable=currentHeightA).grid(column=2, row=3)

currentHeightB = StringVar()
currentHeightLabelB = ttk.Label(mainframe, textvariable=currentHeightB).grid(column=2, row=4)

# 'send command' buttons
ttk.Button(mainframe, text="Send Command", command=sendCommandA).grid(column=4, row=3)
ttk.Button(mainframe, text="Send Command", command=sendCommandB).grid(column=4, row=4)

# 'zero' buttons
ttk.Button(mainframe,text="zero A", command=zeroA).grid(column=1, row=5) 
ttk.Button(mainframe,text="zero B", command=zeroB).grid(column=2, row=5)

# Run the GUI main loop
root.mainloop()
