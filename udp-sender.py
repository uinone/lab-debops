import socket

UDP_IP = "34.64.120.123"
UDP_PORT = 5000
server_addr = (UDP_IP, UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Input: ")
    sock.sendto(message.encode(), server_addr)
    data, addr = sock.recvfrom(1024)
    print("recived message:", data.decode('utf-8'))