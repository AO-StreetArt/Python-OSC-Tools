# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 00:32:12 2016

OSC Hello World Server

@author: alex
"""

from OSC_Base.OscServer import OSC_Server

if __name__ == "__main__":
    
    def print_message(unused_addr, args):
        print('Hello World')
        
    def print_world(unused_addr, args, msg):
        print('%s World' % (msg))
    
    server = OSC_Server()
    server.dispatcher.map("/World", print_message)
    server.dispatcher.map("/Hello", print_world, "Message")
    server.start_server("127.0.0.1", 5005)
    server.serve()