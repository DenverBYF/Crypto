import gmpy2
def phi(k):
	ret=0
	for e in range(1,k+1):
		if gmpy2.gcd(e,k)==1:
			ret+=1
	return ret
	'''
def egcd(a,b):
    if a < b:
        x,y,d = egcd(b,a)
        return y,x,d
    if b == 0:
        return (1,0,a)
    if b == 1:
        return (0,1,1)
    
    x,y,d = egcd(b,a%b)
    x,y = y,(x - y*(a/b))

    return (x,y,d)
'''
def egcd(a,b):
	x,y=0,1
	lx,ly=1,0
	while(b!=0):
		ret,rest=divmod(a,b)
		a,b=b,rest
		x,lx=lx-ret*x,x
		y,ly=ly-ret*y,y
	return lx,ly
def g(a,n,b,m):
    x,y = egcd(m,n)
    d=gmpy2.gcd(m,n)
    if (a - b) % d != 0:
        return 0
    t = (a-b)/d
    return (a - n*y*t) % (m*n/d)

'''
def g(a,n,b,m):
	if (b-a)%gmpy2.gcd(m,n)!=0:
		return 0
	else:
		x,y,d=egcd(max(a,b),min(a,b))
		ret=x*((b-a)/gmpy2.gcd(m,n))*a+n
		return ret'''
def main():
	ret=0
	for n in range(1000000,1005000):
		for m in range(n,1005000):
			ret+=g(phi(n),n,phi(m),m)
			print ret
	print "ret="+str(ret)
if __name__ == '__main__':
	main()