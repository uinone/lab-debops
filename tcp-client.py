import socket

IP = "34.64.120.123"
TCP_PORT = 5001
server_addr = (IP, TCP_PORT)


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_addr)
    MESSAGE = input("Input: ")
    if MESSAGE == 'q':
        break
    s.send(MESSAGE.encode('utf-8'))
    data = s.recv(1024)
    print("recived message:", data.decode('utf-8'))