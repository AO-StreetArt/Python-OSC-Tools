# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:48:15 2016

Python OSC Client

@author: alex
"""

from pythonosc import osc_message_builder
from pythonosc import udp_client

class OSC_Client():
    
    #Initialize the OSC Client
    #param: server_ip - the IP Address of the Server being connected to
    #param: server_port - The Port the OSC Server is listening on
    def __init__(self, server_ip, server_port):
        self.client = udp_client.UDPClient(str(server_ip), str(server_port))

    #Send a message to the OSC Server
    #param: address - The address for the message
    #param: argument_list - a list of the arguments for the message
    def send_message(self, address, argument_list):
        msg = osc_message_builder.OscMessageBuilder(address = str(address))
        for argument in argument_list:
            msg.add_arg(argument)
        msg = msg.build()
        client.send(msg)