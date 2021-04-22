#!/usr/bin/env python3

# inainte de toate trebuie adaugata o regula de ignorare
# a pachetelor RST pe care ni le livreaza kernelul automat
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
import time
from scapy.all import *

ip = IP()
ip.src = '172.10.0.2'
ip.dst = '198.10.0.2'
ip.flags = 0


tcp = TCP()
tcp.sport = 54321
tcp.dport = 10001
tcp.options = [
    ('MSS', 1)
]

## SYN ##
tcp.seq = 100
tcp.flags = 'S'  # flag de SYN
raspuns_syn_ack = sr1(ip / tcp)

tcp.seq += 1
tcp.ack = raspuns_syn_ack.seq + 1
tcp.flags = 'A'
ACK = ip / tcp

sr1(ACK)

time.sleep(2)

tcp.flags = 'PA'
tcp.ack = raspuns_syn_ack.seq + 1
rec = sr(ip / tcp / Raw(load="Hello!"))
print(rec)
# for ch in "salut, lume":
#     tcp.flags = 'PA'
#     tcp.ack = raspuns_syn_ack.seq + 1
#     rcv = sr1(ip / tcp / ch)
#     rcv
#     tcp.seq += 1
