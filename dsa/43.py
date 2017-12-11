from Crypto.Hash import SHA
from gmpy2 import *
anSHA1 = '0954edd5e0afe5542a4adf012611a91912a3ec16'
sha = SHA.new()
sha.update('''For those that envy a MC it can be hazardous to your health
So be friendly, a matter of life and death, just like a etch-a-sketch
''')
H = sha.hexdigest()
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
r0 = 548099063082341131477253921760299949438196259240
s = 857042759984254168557880549501802188789837994940
for k in xrange(65537):
    r = pow(g, k, p) % q
    if r == r0:
        x = (s*k - int(H,16)) * invert(r,q) % q
        print 'x : ', x
        break