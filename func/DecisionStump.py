def DecisionStump(X, Y):
	ErrorRateList = []
	ThetaList = [min(X)]
	SortedX = sorted(X)
	for i in range(len(SortedX)-1):
		ThetaList.append((SortedX[i] + SortedX[i+1])/2)

	for i in range(len(ThetaList)):
		theta = ThetaList[i]
		ErrorRateList.append(ErrorRate(X, Y, theta, 1))
		ErrorRateList.append(ErrorRate(X, Y, theta, -1))

	BestId = ErrorRateList.index(min(ErrorRateList))
	BestTheta, Bests = Decode(ThetaList, BestId)
	return BestTheta, Bests, ErrorRateList[BestId]

def ErrorRate(X, Y, theta, s):
	ErrorCount = 0
	for i in range(len(X)):
		if s * (X[i] - theta) * Y[i] < 0:
			ErrorCount += 1
	return ErrorCount/len(X)

def Decode(ThetaList, Id):
	s = 2*((Id+1)%2)-1
	ThetaId = int(Id/2)
	return ThetaList[ThetaId], s