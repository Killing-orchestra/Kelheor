# -*- coding: utf-8 -*-  

from siphr import Siphr
import binascii
 
siphr = Siphr()
 
K = bytearray("password","utf8")
M = bytearray("ⰦⰦⰦПривет, world!","utf8")
C = siphr.encrypt(K, M)
ss=binascii.hexlify(C)
ss=str(ss)
ss=ss.replace("b'","").replace("'","")
##print(ss)
##print(binascii.unhexlify(ss))
print(ss)
if C==(binascii.unhexlify(ss)):
    print("!!!")
#sss=binascii.unhexlify(ss)
#print(C)
##print(len(C))
##print(str(C))
##b=""
#print(str(C, "utf8"))
##for i in range(len(C)):
##    b+=str(i)
##print(b)
##b = bytearray('', 'utf8')
###b + b'2'

M = siphr.decrypt(K, C)#C=sss
##print(M)
#print(str(M, "utf8"))
