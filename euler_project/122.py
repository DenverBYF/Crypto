def first_chain(x):
	if x == 1:
		return [1]
	if x == 2:
		return [1,2]
	res = []
	arr = [[1,2]]
	while(1):
		temp = []
		for i in arr:
			for j in i:
				p = i[:]
				p.append(i[-1]+j)
				if p[-1] == x:
					return p
				elif p[-1] < x:
					temp.append(p)
		arr = temp[:]


def main():
	s=0
	for i in range(1,201):
		print s
		s+=(len(first_chain(i))-1)
	print s
if __name__ == '__main__':
 	main() 
