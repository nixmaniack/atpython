#!/usr/bin/env python
'''
Author: Muneeb Shaikh <iammuneeb@gmail.com>
License: GPLv3
Created: August 04, 2011
'''
import serial
import time
 
def sendsms(to, message):
  print "Connecting phone"

  ser = serial.Serial('/dev/ttyACM0', 460800, timeout=5)
  time.sleep(1)
  ser.write('ATZ\r')
  time.sleep(1)
  ser.write('AT+CMGF=1\r')
  time.sleep(1)
  ser.write('''AT+CMGS="''' + to + '''"\r''')
  time.sleep(1)
  ser.write(message + "\r")
  time.sleep(1)
  ser.write(chr(26))
  time.sleep(1)
  
  print "disconnecting"
  ser.close()

print "Filling and Sending msg"
sendsms("+919876543210","SMS sent using AT command through Python")
