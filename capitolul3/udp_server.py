import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                     proto=socket.IPPROTO_UDP)

addr = "198.10.0.2"
port = 2222

sock.bind((addr, port))

print(f"Listening on port {port}...")
i = 0
while True:
    if i == 10:
        break
    # data, addr_snd = sock.recvfrom(1)
    # msg += data.decode("utf-8")
    # print(msg)
    # payload = bytes('1', 'utf-8')
    # sent = sock.sendto(payload, addr_snd)

    data, addr_snd = sock.recvfrom(1024)
    msg = data.decode("utf-8")
    print(f"{msg} from {addr_snd}")
    payload = bytes('1', 'utf-8')
    sent = sock.sendto(payload, addr_snd)
    i += 1

sock.close()
