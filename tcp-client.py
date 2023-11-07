import socket

IP = input("Server address: ")
TCP_PORT = 5001
server_addr = (IP, TCP_PORT)
MESSAGE = ''


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_addr)
    MESSAGE = input("Write to server : ")
    if MESSAGE == 'q':
        break
    s.send(MESSAGE.encode('utf-8'))
    print('Sending data:', MESSAGE)
    data = s.recv(1024)
    print("Data from server:", data.decode('utf-8'))

s.close()
