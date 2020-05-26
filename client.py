#!/usr/bin/env python

import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri
from threading import Thread

from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)

t_lim = 0
p_lim = 0

host   = ""
port   = ""
path_t = ""
path_p = ""

def set_uri(id_t, id_p):
    global host, port, path_t, path_p
    uri_t = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/"+id_t
    uri_p = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/"+id_p

    host, port, path_t = parse_uri(uri_t)
    host, port, path_p = parse_uri(uri_p)
    
def set_threshold(threshold_t, threshold_p):
    global t_lim, p_lim
    
    t_lim = threshold_t
    p_lim = threshold_p
    
def getUserInput():
  while 1:
    user_input = raw_input("Change Environment or Reset Thresholds [e/T]: ")    
    
    if user_input != "" and not (user_input == "e" or user_input == "E" or user_input == "t" or user_input == "T"):
        print "Unrecognized character."
        continue
    elif user_input == "E" or user_input == "e":
        user_input = raw_input("ID of Environment: ") # Change environment that it will observer
        set_uri("t" + user_input, "p" + user_input)
    else:
        # Change thresholds already set
        user_input = raw_input("Temperature Threshold: ")
        new_t_lim = int(user_input)
        
        user_input = raw_input("Pressure Threshold: ")
        new_p_lim = int(user_input)
            
        set_threshold(new_t_lim, new_p_lim)

# Get the environment ID from user
while True:
    user_input = raw_input("ID of Environment: ")
    
    if user_input != "":
        set_uri("t" + user_input, "p" + user_input)
        break

# Get thresholds from user
while True:
    user_input = raw_input("Temperature Threshold: ")
    
    if user_input != "":
        new_t_lim = int(user_input)
        
        user_input = raw_input("Pressure Threshold: ")
        
        if user_input != "":
            new_p_lim = int(user_input)
            set_threshold(new_t_lim, new_p_lim)
            break
        
# Create CoAP client        
client = HelperClient(server=(host, port))

# Create thread to get user input
thread = Thread(target = getUserInput)
thread.setDaemon(True)
thread.start()

while True:    
    time.sleep(1)
    
    response_t = client.get(path_t) # get temperature value from server
    response_p = client.get(path_p) # get pressure value from server
    
    t = 0
    p = 0
    
    try:
        t = float(response_t.payload)
        p = float(response_p.payload)
        
        if t > t_lim or p > p_lim: # if temperature and pressure values are above threshold
            sense.clear(red) # turn on all red lights
        else:
            sense.clear() # turn off all leds   
    except:
        print('Sensors not defined or in wrong format') # Error with payload


client.stop()