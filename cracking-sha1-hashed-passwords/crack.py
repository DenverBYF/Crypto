import itertools as its
import hashlib
import time
from numba import jit

@jit
def buster(buster_array):
	chaintext = '67ae1a64661ac8b4494666f58c4822408dd0a3e4'
	for each in buster_array:
		random = its.permutations(list(each),8)
		for each_str in random:	
			each_str = "".join(each_str)	
			tmp = hashlib.sha1(each_str)
			ret = tmp.hexdigest()
			#print "Try "+each_str+"  Sha1 "+ret
			if(ret == chaintext):
				print "Get it :"+each_str
				return 
				
def main():
	start = time.time()
	buster_array = its.product('Qq','Ww','%5','8(','=0','Ii','*+','Nn')
	buster(buster_array)
	end = time.time()
	print "Spend %0.2f s"%(end - start)
if __name__ == '__main__':
	main()