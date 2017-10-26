import gmpy2

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

def g(a,n,b,m):
    x,y,d = egcd(m,n)
    if (a - b) % d != 0:
        return 0
    t = (a-b)/d
    return (a - n*y*t) % (m*n/d)

def prime_sieve(n):
    sieve = [True]*n
    sieve[0] = False
    sieve[1] = False
    for i in xrange(n):
        if not sieve[i]:
            continue
        for j in xrange(i+i,n,i):
            sieve[j] = False
    return sieve

def primes_up_to(n):
    sieve = prime_sieve(n)
    return [x for x in xrange(n) if sieve[x]]

def factor_out(n,f):
    r = 0
    while n % f == 0:
        r += 1
        n /= f
    return r

def totient_sieve(n):
    primes = primes_up_to(n)
    sieve = [1]*n
    for p in primes:
        for j in xrange(p,n,p):
            r = factor_out(j,p)
            sieve[j] *= p**(r-1)*(p - 1)
    return sieve
def phi(k):
    ret=0
    for e in range(1,k+1):
        if gmpy2.gcd(e,k)==1:
            ret+=1
    return ret
def e531(a,b):
    result=0
    for m in xrange(a,b):
        for n in xrange(a,m):
            x = g(phi(n),n,phi(m),m)
            #assert x == 0 or x % n == totient[n] and x % m == totient[m]
            result += x
            print result
    return result
if __name__ == '__main__':
    print e531(1000000,1005000)