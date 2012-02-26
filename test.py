import cross_finder

def strat_reverse_calc(parOne, parTwo, timeStart, timeEnd):
	crosses = cross_finder.find(parOne, parTwo, timeStart, timeEnd)
	
	start_course = crosses[0][1]
	
	dif = 0
	
	for i in range(1,len(crosses)):
		if crosses[i][2] == 'First2Up':
			toAdd = crosses[i-1][1]-crosses[i][1]
		else:
			toAdd = -crosses[i-1][1]+crosses[i][1]

		dif += toAdd
	dif/=start_course
	return dif