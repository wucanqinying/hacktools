from scapy.layers.inet import ICMP, UDP, TCP
from whois import whois
import socket

from scapy.all import *
from random import randint

import time

def main():

    while 1 :
        pdst = "%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
        psrc = "192.168.249.222"
        send(IP(src=psrc,dst=pdst)/TCP(dport=80,flags='S'))
        time.sleep(0.5)
        print(pdst)

if __name__ == '__main__':
    main()