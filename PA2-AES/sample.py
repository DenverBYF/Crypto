from oracle import *
import sys
import itertools as its
ret=[]
cur=[]
def tohex(num):
	if len(hex(num)[2:])==2:
		return hex(num)[2:]
	else:
		return "0"+hex(num)[2:]
def buster(iv,ctext,buster_array):
	global ret,cur
	for i in range(1,17):		
		for each in buster_array:
			iv_tmp="00"*(16-i)
			iv_tmp+="".join(each)
			if i>1:
				for j in range(i-1):
					iv_tmp+=tohex(cur[-(j+1)]^i)
			ctext_tmp=iv_tmp+ctext
			if send_data(ctext_tmp,iv,i)==1:
				print ret
				break
def send_data(data,iv,j):
	global ret,cur		
	ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]

	Oracle_Connect()

	rc = Oracle_Send(ctext, 2)
	print "try : "+data
	if rc==1:
		tmp=int("0x"+data[(16-j)*2:(16-j)*2+2],16)^j^int("0x"+iv[(16-j)*2:(16-j)*2+2],16)
		ret.append(chr(tmp))
		cur.append(int("0x"+data[(16-j)*2:(16-j)*2+2],16)^j)
		return 1
	Oracle_Disconnect()
def main():
	global ret,cur
	f = open('challenge-ciphertext.txt')
	data = f.read()
	f.close()
	buster_array=[]
	tmp=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	iv=data[:32]
	ctext=data[32:64]
	buster(iv,ctext,list(its.product(tmp,repeat=2)))
	iv_2=ctext
	ctext_2=data[64:96]
	cur=[]
	buster(iv_2,ctext_2,list(its.product(tmp,repeat=2)))
	plain_1=ret[:16]
	plain_2=ret[16:]
	plain_1.reverse()
	plain_2.reverse()
	plain=plain_1+plain_2
	print "Plaintext is : "+"".join(plain)
	'''
	ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
	#print ctext

	Oracle_Connect()

	rc = Oracle_Send(ctext, 3)
	print rc
	Oracle_Disconnect()
'''
if __name__ == '__main__':
	main()
