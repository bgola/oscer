#!/usr/bin/env python

from pythonosc import udp_client

import ast

def guess_osc_type(string):
    try:
        return ast.literal_eval(string)
    except:
        return string

def send_osc(ip, port, address, values):
    client = udp_client.SimpleUDPClient(ip, port)
    client.send_message(address, values)
