from func.DecisionStump import *
from func.GenerateData import *

ExperimentCount = 5000	#input("Repeat Experiment for ____ times:")
Datasize = 20			#input("Data Size:")

Error_inList = []
Error_outList = []
ThetaList = []
sList = []
for Experiment in range(ExperimentCount):
	#Generate Data
	X = GenerateX(Datasize, -1, 1)
	Y = GenerateY(X, 0.2)

	#Run Decision Stump On Data
	theta, s, CurError_in = DecisionStump(X, Y)
	CurError_out = 0.5 + 0.3*s*(abs(theta)-1)
	Error_inList.append(CurError_in)
	Error_outList.append(CurError_out)
	ThetaList.append(theta)
	sList.append(s)

print(sum(Error_inList)/ExperimentCount)
print(sum(Error_outList)/ExperimentCount)