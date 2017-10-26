import collections
code=[]
key=[]
def get_code():
	global code
	with open('59.txt','r') as f:
		 code=f.read().split(',')
def main():
	global code
	global key
	get_code()
	p1=collections.Counter(code[::3])
	p2=collections.Counter(code[1::3])
	p3=collections.Counter(code[2::3])
	key.append(int(max(zip(p1.values(),p1.keys()))[1])^32)
	key.append(int(max(zip(p2.values(),p2.keys()))[1])^32)
	key.append(int(max(zip(p3.values(),p3.keys()))[1])^32)
	ret=0
	for i in range(3):
		ret+=sum(int(code[j])^key[i] for j in range(i,len(code),3))
	print ret
if __name__ == '__main__':
	main()