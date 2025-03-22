from scapy.layers.inet import ICMP, UDP
from whois import whois
import socket

from scapy.all import *
from random import randint

import time


def main():
    ip = "192.168.249.12"

    ans, uans = sr(IP(dst=ip) / UDP(dport=80))

    for snd, rcv in ans:
        print(rcv.sprintf("%IP.src% is up"))

    pass

if __name__ == '__main__':
    main()