from Crypto.Cipher import DES3
import re
def main():
	with open('a.txt','r') as f:
		data = f.read().split()
	ct = "".join(data)
	N = 0
	for buster in range(999999):
		buster_key = 'COPACOBANA'+str(buster).zfill(6)
		modal = DES3.new(buster_key, DES3.MODE_CBC, IV=('0'*16).decode('hex'))
		pt = modal.decrypt(ct.decode('hex')[:2352])
		word_len = len(re.findall('[a-zA-Z]',pt))
		if word_len > N:
			N = word_len
			print "Plaintext : "+pt 
			print "\n"*3
if __name__ == '__main__':
	main()