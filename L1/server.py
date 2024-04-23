import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("172.30.114.12",5555))
buff,addr=s.recvfrom(10)
print(buff)
s.sendto("hello", addr)