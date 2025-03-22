from scapy.layers.inet import ICMP
from whois import whois
import socket

from scapy.all import *
from random import randint

import time

def main():
    ip = "192.168.249.122"
    dport = randint(1,65535)    #设置随机端口
    packet = IP(dst=ip)/TCP(flags="A",dport=dport)   #构建数据包
    response = sr1(packet, timeout=1.0,verbose=0)   #发送数据包，接受回包
    if response:    #如果有回复的话，进行判断
        #是否存在RST的标志位（TCP三次握手）
        if int(response[TCP].flags)==4:
            time.sleep(0.5)
            print(ip+' is up')
        else:
            print(ip+' is down')
    else:
        print(ip+' is down')
    pass

if __name__ == '__main__':
    main()