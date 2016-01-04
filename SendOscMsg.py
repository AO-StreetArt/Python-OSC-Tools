# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:50:24 2016

Basic Command Line Tool to send an OSC Message

@author: alex
"""

import sys
from OSC_Base.OscClient import OSC_Client
import logging

if __name__ == "__main__":
    
    #Handle the Input Parameters
    if len(sys.argv) == 1:
        
        print("Input Parameters:")
        print("Server IP: The Server IP to connect to")
        print("Server Port: The Server Port to connect to")
        print("Log File: The file name to write the logs out to")
        print("Log Level: Debug, Info, Warning, Error")
        print("Address: The Address on the message")
        print("Arguments: A Series of Arguments to be passed in the message")
        print("Example: ")
        
    elif sys.argv[1] == "help":
        print("Input Parameters:")
        print("Server IP: The Server IP to connect to")
        print("Server Port: The Server Port to connect to")
        print("Log File: The file name to write the logs out to")
        print("Log Level: Debug, Info, Warning, Error")
        print("Address: The Address on the message")
        print("Arguments: A Series of Arguments to be passed in the message")
        print("Example: ")
        
    elif len(sys.argv) < 6:
        
        print("Not enough Input Parameters")
        
    else:
        
        #Set up the file logging config
        if sys.argv[4] == 'Debug':
            logging.basicConfig(filename=sys.argv[3], level=logging.DEBUG)
        elif sys.argv[4] == 'Info':
            logging.basicConfig(filename=sys.argv[3], level=logging.INFO)
        elif sys.argv[4] == 'Warning':
            logging.basicConfig(filename=sys.argv[3], level=logging.WARNING)
        elif sys.argv[4] == 'Error':
            logging.basicConfig(filename=sys.argv[3], level=logging.ERROR)
        else:
            print("Log level not set to one of the given options, defaulting to debug level")
            logging.basicConfig(filename=sys.argv[3], level=logging.DEBUG)
        
        #Create the client
        logging.debug("Creating OSC Client with IP %s and Port %s" % (sys.argv[1], sys.argv[2]))
        client = OSC_Client(sys.argv[1], sys.argv[2])
        
        #Build the argument list
        argument_list = []
        i = 0
        for i in range(6, len(sys.argv)):
            logging.debug("Adding argument %s" % (sys.argv[i]))
            argument_list.append(str(sys.argv[i]))
        
        #Send the message
        client.send_message(sys.argv[5], argument_list)
        logging.debug("Message Sent")