def init(fileName):
	global times
	global closes
	
	fileIn=open(fileName)
	lines=fileIn.readlines()[1:]
	fileIn.close()
	
	times = []
	closes = []
	for line in lines:
		values = line.split(',')
		times.append(values[2] + '_' + values[3])
		closes.append(float(values[7]))