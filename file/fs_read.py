
fs_name = 'write.txt'
pv_count = 0

with open(fs_name) as f:
	while True:
		line=f.readline()
		if len(line)==0:
			break
		elif(',' in line):
			print(line, end=':')
		

