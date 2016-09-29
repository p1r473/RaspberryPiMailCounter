#!/usr/bin/python
#cat <<! > raspi-gmail.py

import imaplib, time
import os, sys
import urllib2
import signal
import atexit


from Adafruit_7Segment import SevenSegment

#from Adafruit_LED_Backpack import SevenSegment
#display = SevenSegment.SevenSegment()
#display.begin()

segment = SevenSegment(address=0x70)

def exit_handler():
    #Handles CTRL+C
    segment.clear()

def get_num(x):

    return int(''.join(ele for ele in x if ele.isdigit()))

def handler(signum, frame):
    #Handles CTRL+Z
    segment.clear()
    exit()

def on_exit(sig, func=None):
    segment.clear()


#print numEmailsString

print "Press CTRL+Z or CTRL+C to exit"

#Handles CTRL+C
atexit.register(exit_handler)

# Continually update the time on a 4 char, 7-segment display

while(True):

    #handles CTRL+Z
    signal.signal(signal.SIGTSTP, handler)
    #while False:
    #   pass

    req = urllib2.Request('https://script.google.com/macros/s/XXX/exec')
    response = urllib2.urlopen(req)
    the_page = response.read()
    numEmails = get_num(the_page)
    numEmailsString = str(numEmails).rjust(4)

    
    segment.writeDigit(0, int(numEmailsString[0]))   
    segment.writeDigit(1, int(numEmailsString[1]))   
    segment.writeDigit(3, int(numEmailsString[2])) 
    segment.writeDigit(4, int(numEmailsString[3]))
    #time.sleep(10)
    #segment.clear()

    # Wait one second
    time.sleep(300)
