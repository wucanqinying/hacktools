from scapy.layers.inet import ICMP, UDP, TCP
from whois import whois
import socket

from scapy.all import *
from random import randint

import time

def main():
    ip = "192.168.249.12"

    port = 80

    packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")

    resp = sr1(packet,timeout=20)

    if(str(type(resp))=="<type 'NoneType'>"):#确实是否有数据返回，要是没返回，说明主机挂了
        print("port %s is closed"%(port))
    elif(resp.haslayer(TCP)):  #确认是否有TCP层
        if(resp.getlayer(TCP).flags == 0x12): #确认返回是否有ack的标志值（0x12）
            send_rst = sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="AR"),timeout=20) #AR是ack的response
            print("port %s is open"%(port))
        elif(resp.getlayer(TCP).flags == 0x14): #主机端拒绝了建立关系
            print("port %s is down" % (port))



if __name__ == '__main__':
    main()