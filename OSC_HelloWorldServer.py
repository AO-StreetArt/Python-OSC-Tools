# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 00:32:12 2016

OSC Hello World Server

@author: alex
"""

from OSC_Base.OscServer import OSC_Server

if __name__ == "__main__":
    
    def print_message(unused_addr):
        print('Hello World')
        
    def print_world(unused_addr, args, msg, msg2):
        print('%s World' % (msg))
        print('%s Pudding' % (msg2))
        for arg in args:
            print(arg)
    
    server = OSC_Server()
    server.dispatcher.map("/World", print_message)
    server.dispatcher.map("/Hello", print_world, "Message", "Message2")
    server.start_server("127.0.0.1", 5005)
    server.serve()