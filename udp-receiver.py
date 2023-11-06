import socket

UDP_IP = "10.178.0.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message:", data.decode('utf-8'), "from ", addr)
    sock.sendto(data,addr)