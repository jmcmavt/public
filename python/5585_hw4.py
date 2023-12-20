# ECE 5585 HW4 Python Template - Permission granted to post publicly

from scapy.all import *
import time # you need this to implement the sleep function

# vars

source_1 = "1.1.1.1" # change these to an IP address in dotted decimal format and keep the quotes
source_2 = "2.2.2.2" 
destination_1 = "3.3.3.3"

# format your function like the below

# packet = PROTOCOL(src=SOURCE, dst=DESTINATION)/PROTOCOL(sport=SOURCEPORTVALUE,dport=DESTPORTVALUE,flags=FLAGVALUE)

def packet_craft():
  packet = IP(src=source_1, dst=destination_1)/TCP(sport=707, dport=1337, flags=20)/"Hello World"
  send(packet, count=10)

# this function will send an IP packet from source_1 to destination_1 using the TCP protocol to destination port 1337 with payload "Hello World"
# the flags should be represented as a decimal value, here is a resource that will help
# https://www.manitonetworks.com/flow-management/2016/10/16/decoding-tcp-flags

# if you need to increment packets (like to destination ports) there might be a built in way to do it in scapy (which probably uses a loop) or you can use a loop

def loop_packet():
  source_port = 1337
  while source_port < 1400:
    packet = # craft your packet here
    send(packet)
    source_port = source_port + 1

# you can add your sleep time when the program runs

packet_craft()
time.sleep(5)
loop_packet()
time.sleep(5)
