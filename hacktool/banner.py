from scapy.layers.inet import ICMP, UDP, TCP
from whois import whois
import socket

from scapy.all import *
from random import randint

import time


def main():
    ip = "192.168.249.12"
    port = 5357
    s = socket.socket()
    s.connect((ip, port))
    s.send('haha'.encode())
    banner = s.recv(1024)
    s.close()
    print("banner is {}".format(banner))
    pass

if __name__ == '__main__':
    main()