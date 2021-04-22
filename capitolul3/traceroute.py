import socket
import traceback
import requests
import json


def get_location_info(ip):
    response = requests.get("http://ip-api.com/json/" + ip)

    response = json.loads(response.text)
    status = response['status']

    if status != 'fail':
        oras = response['city']
        regiune = response['regionName']
        tara = response['country']

        return oras, regiune, tara

# print(get_location_info('124.225.206.22'))


def createSender(ttl):
    udp_send_sock = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
    udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
    return udp_send_sock


def createReceiver(port):
    icmp_recv_socket = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    icmp_recv_socket.settimeout(10)
    try:
        icmp_recv_socket.bind(('172.10.0.2', port))
    except socket.error as e:
        raise IOError('Unable to bind receiver socket: {}'.format(e))

    return icmp_recv_socket


def traceroute(ip, port):
    ttl = 10
    # while True:

    udp_send_sock = createSender(ttl)
    icmp_recv_socket = createReceiver(port)

    udp_send_sock.sendto(b'', (ip, port))

    addr = 'done!'
    try:
        data, addr = icmp_recv_socket.recvfrom(1024)
    except Exception as e:
        print("Socket timeout ", str(e))
        print(traceback.format_exc())
    print(get_location_info(addr[0]))


traceroute("124.225.206.22", 33434)
