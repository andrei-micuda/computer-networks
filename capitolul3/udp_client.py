import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                     proto=socket.IPPROTO_UDP)

addr = "127.0.0.1"
port = 10011

msg = "hello from client"

for char in msg:
    sent = sock.sendto(char.encode('utf-8'), (addr, port))
    data, addr_recv = sock.recvfrom(1)
    print(data)

sock.close()
