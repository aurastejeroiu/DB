import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"Stejeroiu Aura",("172.30.113.250",7777))
print(s.recvfrom(10))