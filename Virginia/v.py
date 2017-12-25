from __future__ import division  
import math
import hashlib

with open('ct.txt', 'r') as c:
	ct = c.read().lower()
ctl = len(ct)
freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
key_len = 0
key = ''
pt = ''
count = [0]*26

for best_len in range(1,7):
	ret = 0
	for j in range(best_len):
		for i in range(26):
			count[i] = 0
		for i in range(j, ctl, best_len):
			count[ord(ct[i]) - 97] += 1
		ic = 0
		num = ctl/best_len
		for i in range(len(count)):
			ic += math.pow(count[i]/num, 2)
		ret += ic
	if ret/best_len > 0.065:
		key_len = best_len
		print "len of key is "+str(best_len);

for j in range(key_len):
	for i in range(26):
		count[i] = 0
	for i in range(j, ctl, key_len):
		count[ord(ct[i]) - 97] += 1
	max_dp = 0
	best_i = 0
	for i in range(26):
		cur_dp = 0
		for k in range(26):
			cur_dp += freq[k] * count[(k+i)%26]
			#print cur_dp
		if (cur_dp > max_dp):
			#print i
			max_dp = cur_dp
			best_i = i
	key += chr(best_i + 97)
print "Key is "+key 		

ascii='abcdefghijklmnopqrstuvwxyz'
for i in range(ctl):
    j = i % key_len
    k = ascii.index(key[j])
    m = ascii.index(ct[i])
    if m < k:
        m += 26
    pt += ascii[m-k]
    i += 1
print "answer is "+hashlib.sha1(pt).hexdigest()


