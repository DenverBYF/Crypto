def tohex(num):
	if len(hex(num)[2:])==2:
		return hex(num)[2:]
	else:
		return "0"+hex(num)[2:]
print tohex(22)