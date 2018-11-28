from func.DecisionStump import *
import numpy as np

#Read Train Data
File_Data_train = open("./Data/Data_train.dat", "r")
Data_train_X, Data_train_Y = [], []
if File_Data_train.mode == "r":
	fl = File_Data_train.readlines()
	for line in fl:
		Data_train = line.split()
		Dim = len(Data_train)-1
		Data_train_X.append([float(i) for i in Data_train[0:Dim]])
		Data_train_Y.append(int(Data_train[-1]))
File_Data_train.close()

Data_train_X = np.array(Data_train_X).T

#Run MultiDimension Decision Stump
from func.MultiDimensionDecisionStump import *
theta, s, Error, BestDim = Train(Data_train_X, Data_train_Y)
print(theta, s, Error, BestDim)

#Read Test Data
File_Data_test = open("./Data/Data_test.dat", "r")
Data_test_X, Data_test_Y = [], []
if File_Data_test.mode == "r":
	fl = File_Data_test.readlines()
	for line in fl:
		Data_test = line.split()
		Dim = len(Data_test)-1
		Data_test_X.append([float(i) for i in Data_test[0:Dim]])
		Data_test_Y.append(int(Data_test[-1]))
File_Data_test.close()

Data_test_X = np.array(Data_test_X).T

E_out = Test(Data_test_X, Data_test_Y, theta, s, BestDim)
print(E_out)