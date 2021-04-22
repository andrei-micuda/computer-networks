from scapy.all import *
from netfilterqueue import NetfilterQueue as NFQ
import os

os.system("iptables -I FORWARD -j NFQUEUE --queue-num 5")


def alter_packet(pachet):
    scapy_packet = IP(pachet.get_payload())
    # print(scapy_packet.summary())
    payload = scapy_packet["TCP"].payload
    if len(payload) > 0:
        print(payload)
    else:
        print("no payload")
    return pachet


def proceseaza(pachet):
    octeti = pachet.get_payload()
    scapy_packet = IP(octeti)
    # print("Pachet: ", scapy_packet.summary())
    # pachet = alter_packet(pachet)
    # pachet.set_payload(bytes(pachet.get_payload()))
    pachet.accept()


queue = NFQ()
try:
    os.system("iptables -I FORWARD -j NFQUEUE --queue-num 5")
    queue.bind(5, proceseaza)
    queue.run()
except KeyboardInterrupt:
    queue.unbind()