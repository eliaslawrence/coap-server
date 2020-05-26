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

uri_a = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/add" # URI to create resources
host, port, path_a = parse_uri(uri_a)

print host
print port

client = HelperClient(server=(host, port))

def set_uri(id_t, id_p):
    global path_t, path_p
    uri_t = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/"+id_t
    uri_p = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/"+id_p

    host, port, path_t = parse_uri(uri_t)
    host, port, path_p = parse_uri(uri_p)

def getUserInput():
  while 1:
    user_input = raw_input("Change or Add Environment? [c/A]: ")    
    
    if user_input != "" and not (user_input == "c" or user_input == "C" or user_input == "a" or user_input == "A"):
        print "Unrecognized character."
        continue
    elif user_input == "c" or user_input == "C":
        # Change to environment with resources already created 
        user_input = raw_input("ID of Environment: ")
        set_uri("t" + user_input, "p" + user_input)
    else:
        # Create new environment
        user_input = raw_input("ID of NEW Environment: ")
        client.post(path_a, "t" + user_input) # Create resource for temperature sensor
        client.post(path_a, "p" + user_input) # Create resource for pressure sensor
            
        set_uri("t" + user_input, "p" + user_input)

# Get the environment ID from user
while True:
    user_input = raw_input("Set or Add Environment? [s/A]: ")
    
    if user_input != "" and not (user_input == "s" or user_input == "S" or user_input == "a" or user_input == "A"):
        print "Unrecognized character."
        continue
    elif user_input == "s" or user_input == "S":
        # Set to environment with resources already created 
        user_input = raw_input("ID of Environment: ")
        set_uri("t" + user_input, "p" + user_input)
        break
    else:
        # Create new environment
        user_input = raw_input("ID of NEW Environment: ")
        client.post(path_a, "t" + user_input) # Create resource for temperature sensor
        client.post(path_a, "p" + user_input) # Create resource for pressure sensor
            
        set_uri("t" + user_input, "p" + user_input)
        break
        
# Create thread to get user input
thread = Thread(target = getUserInput)
thread.setDaemon(True)
thread.start()

while True:    
    time.sleep(1)
    
    # Get values from emulator
    t = sense.get_temperature()
    p = sense.get_pressure()
    
    # Send values to the server
    client.post(path_t, str(t))
    client.post(path_p, str(p))


client.stop()