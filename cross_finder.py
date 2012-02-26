import simple_average

def find(parOne, parTwo, timeStart, timeEnd) :
	splineOne = simple_average.simple_average(parOne, timeStart, timeEnd)
	splineTwo = simple_average.simple_average(parTwo, timeStart, timeEnd)
	
	fw = open('spline.csv', "w")
	for i in range(len(splineOne)):
		fw.write(splineOne[i][0]+','+str(splineOne[i][1])+','+str(splineTwo[i][1])+'\n')
	fw.close()
	
	# spline One and spline are equal at length
	OneIsUp = True;
	if splineOne[0][1] > splineTwo[0][1]:
		OneIsUp = True
	else:
		OneIsUp = False
		
	crosses = []
	for i in range(len(splineOne)):
		if splineOne[i][1] > splineTwo[i][1]:
			if OneIsUp == False:
				crosses.append([splineOne[i][0], splineOne[i][2], 'First2Up'])
				OneIsUp = True
		else:
			if OneIsUp == True:
				crosses.append([splineOne[i][0], splineOne[i][2], 'First2Down'])
				OneIsUp = False
	
	return crosses