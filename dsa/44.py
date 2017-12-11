import re
from gmpy2 import *
from Crypto.Hash import SHA
with open('44.txt','r') as fp:
    data = re.findall('msg: (.+)\ns: (.+)\nr: (.+)\nm: (.+)', fp.read())
    r = [i[2] for i in data]

p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
anSHA1 = 'ca8f6f7c66fa362d40760d135b763eb8527d3d52'
for ri in set(r):
    same_k = filter(lambda x : ri==x[2], data)
    if len(same_k)==2:
        m1 = int(same_k[0][0].encode('hex'),16)
        m2 = int(same_k[1][0].encode('hex'),16)
        s1 = int(same_k[0][1])
        s2 = int(same_k[1][1])
        H1 = int(same_k[0][3],16)
        H2 = int(same_k[1][3],16)
        k = ((H1 - H2) * invert(s1-s2,q))%q
        r = int(same_k[0][2])
        x = (s1*k - H1) * invert(r,q) % q
        print 'x :', x
        break