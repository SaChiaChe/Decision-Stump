def Train(X, Y):
	from .DecisionStump import DecisionStump
	Dim = len(X)

	BestCut = []
	E_inList = []
	for i in range(Dim):
		theta, s, CurErrorRate = DecisionStump(X[i], Y)
		BestCut.append([theta, s])
		E_inList.append(CurErrorRate)
	
	BestId = E_inList.index(min(E_inList))
	return BestCut[BestId][0], BestCut[BestId][1], E_inList[BestId], BestId

def Test(X, Y, theta, s, Dim):
	Error = 0
	BestX = X[Dim]
	Datasize = len(Y)
	for i in range(Datasize):
		Predict = s*(BestX[i]-theta)
		if Y[i]*Predict < 0:
			Error += 1
	return Error/Datasize