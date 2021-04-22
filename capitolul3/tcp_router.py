import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,
                     proto=socket.IPPROTO_TCP)

addr = "172.10.0.2"
port = 10_000

sock.bind((addr, port))
sock.listen(2)

print(f"Listening on port {port}...")
msg = ""
while True:
    connection, addr_snd = sock.accept()
    data = connection.recv(1)
    msg += data.decode("utf-8")
    print(msg)
    payload = bytes('1', 'utf-8')
    sent = connection.send(payload)

sock.close()
