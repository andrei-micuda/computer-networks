from scapy.all import *

pkt = IP(
    src="8.8.8.8",
    dst="198.10.0.2") / UDP(dport=2222) / Raw(load="abc")

sr(pkt)
