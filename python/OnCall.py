#!/usr/bin/env python3

# A silly early project I made to configure LED lights on a raspberry pi to show my work status to 
# my wife while working from home

import RPi.GPIO as GPIO
import time

ledPinB = 29    # Blue LED
ledPinY = 36    # Yellow LED
ledPinR = 12    # Red LED
ledPinG = 38    # Green LED

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPinY, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinY, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(ledPinR, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinR, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(ledPinG, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinG, GPIO.LOW) # make ledPin output LOW level
    GPIO.setup(ledPinB, GPIO.OUT)
    GPIO.output(ledPinB, GPIO.LOW)

# Each of these functions turns off the specified LED, blue will probably not be used

def lightoff_b():
    GPIO.output(ledPinB, GPIO.LOW)
    
def lightoff_y():
    GPIO.output(ledPinY, GPIO.LOW)

def lightoff_r():
    GPIO.output(ledPinR, GPIO.LOW)

def lightoff_g():
    GPIO.output(ledPinG, GPIO.LOW)

def lightoff_all():
    lightoff_b()
    lightoff_y()
    lightoff_r()
    lightoff_g()

def lightg_init():
    for i in range (4):
        GPIO.output(ledPinG, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPinG, GPIO.LOW)
        time.sleep(0.5)
        
def lighty_init():
    for i in range (4):
        GPIO.output(ledPinY, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPinY, GPIO.LOW)
        time.sleep(0.5)

def lightr_init():
    for i in range (4):
        GPIO.output(ledPinR, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPinR, GPIO.LOW)
        time.sleep(0.5)
        

lightoff = 0 # Will shut the light off if user presses S
choice = 0 # Choice of User LED


setup()
print("Initializing OnCall Status Indicator..", end = ".")
time.sleep(2)
GPIO.output(ledPinB, GPIO.HIGH)
print("system ready!\n")    

while choice != 'Q':
    print("Press:\n 'R' for 'On Conference Call'\n 'Y' for 'Headphones On'\n 'G' for 'Available'\n\nPress 'Q' to quit.\n")
    lightoff = 0
    choice = input("Your selection: ")
    choice = choice.upper()
    if choice == 'G':
        while lightoff != 'S':
            lightg_init()
            GPIO.output(ledPinG, GPIO.HIGH)
            lightoff = input("You're available, press 'S' then 'Enter' to stop.")
            lightoff = lightoff.upper()
            GPIO.output(ledPinG, GPIO.LOW)
        continue
    elif choice == 'R':
        while lightoff != 'S':
            lightr_init()
            GPIO.output(ledPinR, GPIO.HIGH)
            lightoff = input("You're on a conference call, press 'S' then 'Enter' to stop.")
            lightoff = lightoff.upper()
            GPIO.output(ledPinR, GPIO.LOW) 
        continue
    elif choice == 'Y':
        while lightoff != 'S':
            lighty_init()
            GPIO.output(ledPinY, GPIO.HIGH)
            lightoff = input("You have headphones on, press 'S' then 'Enter' to stop.")
            lightoff = lightoff.upper()
            GPIO.output(ledPinY, GPIO.LOW)  
        continue
    else:
        print("Goodbye")
        lightoff_all()
        break
