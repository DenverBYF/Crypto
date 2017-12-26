import gmpy2

n1 = 9051013965404084482870087864821455535159008696042953021965631089095795348830954383127323853272528967729311045179605407693592665683311660581204886571146327720288455874927281128121117323579691204792399913106627543274457036172455814805715668293705603675386878220947722186914112990452722174363713630297685159669328951520891938403452797650685849523658191947411429068829734053745180460758604283051344339641429819373112365211739216160420494167071996438506850526168389386850499796102003625404245645796271690310748804327
n2 = 13225948396179603816062046418717214792668512413625091569997524364243995991961018894150059207824093837420451375240550310050209398964506318518991620142575926623780411532257230701985821629425722030608722035570690474171259238153947095310303522831971664666067542649034461621725656234869005501293423975184701929729170077280251436216167293058560030089006140224375425679571181787206982712477261432579537981278055755344573767076951793312062480275004564657590263719816033564139497109942073701755011873153205366238585665743
e = 65537

with open('ct.txt', 'r') as c:
	ct1 = int(c.readline())
	ct2 = int(c.readline())

def gcd(a, b):
	if a < b:
		a, b = b, a
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a
p = gcd(n1, n2)
q1 = n1/p
q2 = n2/p

n1 = p*q1
n2 = p*q2

N1 = (p-1)*(q1-1)
N2 = (p-1)*(q2-1)

d1 = long(gmpy2.invert(e, N1))
d2 = long(gmpy2.invert(e, N2))

m1 = pow(ct1, d1, n1)
m2 = pow(ct2, d2, n2)

print "ret is "+ str(m1 + m2)
