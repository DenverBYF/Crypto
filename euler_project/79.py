import collections
code=[]
num=set()
def get_code():
	global code
	with open('79.txt','r')as f:
		code=f.read().split('\n')
def get_num():
	global code,num
	for each_word in code:
		for each_num in each_word:
			num.add(each_num)
def get_order(word):
	for i in range(len(word)-1):
		for j in range(i+1,len(word)):
			yield word[i],word[j]
def make_tree():
	global code,num
	node=collections.defaultdict(set)
	for each in code:
		for i,j in get_order(each):
			node[i].add(j)
	return node
def order(node):
	for each in node.items():
		node[each[0]]=len(each[1])
	ret_list=sorted(node.items(), key=lambda node: node[1],reverse=True)
	ret=""
	for each in ret_list:
		ret+=str(each[0])
	print ret 
def main():
	global num,code
	ret=[]
	get_code()
	get_num()
	node=make_tree()
	order(node);

if __name__ == '__main__':
	main()