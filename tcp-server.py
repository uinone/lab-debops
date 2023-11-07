import socket
import time

IP = "10.178.0.2"
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data:
        break
    currentTime = " " + time.ctime(time.time()) + "\r\n"
    data = data + currentTime.encode('ascii')
    conn.send(data)
    conn.close()
    print("received message:", data.decode('utf-8'), "from ", addr)
conn.close()