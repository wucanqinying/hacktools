from scapy.layers.inet import ICMP
from whois import whois
import socket

from scapy.all import *
from random import randint

def main():
    ans,uans = sr(IP(dst="192.168.249.12")/TCP(dport=80,flags="S"))

    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% 80 is up"))

    pass

if __name__ == '__main__':
    main()