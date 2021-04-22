import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

addr = "198.10.0.2"
port = 10_001

msg = "hello from client"

sock.connect((addr, port))

sent = sock.send(msg.encode("utf-8"), (addr, port))
data, addr_recv = sock.recv(1024)
print(data)

sock.close()
