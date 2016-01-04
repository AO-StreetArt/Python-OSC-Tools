# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:34:54 2016

Python OSC Server

@author: alex
"""

from pythonosc import dispatcher
from pythonosc import osc_server

class OSC_Server():

    #Initialize the OSC Server    
    def __init__(self):
        #Start the dispatcher
        self.dispatcher = dispatcher.Dispatcher()
        
    #Once the dispatcher has been  mapped, we can start the server
    def start_server(self, ip, port):
        #Start the server
        self.server = osc_server.ThreadingOSCUDPServer((ip, port), self.dispatcher)
        
    #Once the server is started, we can start serving requests
    def serve(self):
        #Serve Forever
        self.server.serve_forever()