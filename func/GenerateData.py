def GenerateX(Size, LowerBound, UpperBound):
	from random import uniform
	DataX = []
	for i in range(Size):
		DataX.append(uniform(float(LowerBound), float(UpperBound)))

	return DataX

def GenerateY(DataX, P_noise):
	DataY = []
	for i in DataX:
		y = 1 if i >= 0 else -1
		from random import uniform
		if uniform(0, 1) < P_noise:
			y = -y
		DataY.append(y)

	return DataY