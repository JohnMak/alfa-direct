def simple_average(par, timeStart, timeEnd):
	from data import times
	from data import closes
		
	if timeStart == '':
		start = par
	else:
		start = times.index(timeStart)
	if timeEnd == '':
		end = len(times)-1
	else:
		end = times.index(timeEnd)
		
	def average(i, period):
		if period > i+1:
			period = i+1
		return sum(closes[i+1-period:i+1])/period

	spline = []

	for i in range(start,end+1):
		spline.append([times[i], average(i,par), closes[i]])
	
	return spline