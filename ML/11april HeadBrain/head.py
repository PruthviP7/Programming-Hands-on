#User Defined Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MeanData(arr):
	size = len(arr)
	sum = 0 
	
	for i in range(size):
		sum = sum + arr[i]

	return (sum/size)

def MarvellousHeadBrain(Name):
	dataset = pd.read_csv(Name)
	print("Size of our data set is",dataset.shape)

	X = dataset["HeadSize(cm^3)"].values
	Y = dataset["Brain Weight(grams)"].values

	print("Length of X",len(X))
	print("Length of Y",len(Y))

	Mean_X = MeanData(X)
	Mean_Y = MeanData(Y)

	print("Mean of Independent variable is ",Mean_X)
	print("Mean of Dependent variable is ",Mean_Y)
	
	# m = (sum(X- Xb)*(Y-Yb))/Sum(X-Xb)^2
	numerator = 0
	denominator = 0

	for i in range(len(X)):
		numerator = numerator  + (X[i] - Mean_X)*(Y[i] - Mean_Y)
		denominator = denominator + (X[i] - Mean_X)**2

	m = numerator / denominator
	print("Value of slope is",m)
		
	#Y = mX + c
	#c = Y - mX
	#c = Mean_Y - (m*Mean_X)
	c = Mean_Y - (m*Mean_X)
	print("Value of Y intercept is",c)

	X_Start = np.min(X) - 200	#we can skip this 200
	X_End = np.max(X) + 200

	x = np.linspace(X_Start,X_End)
	y = m*x + c

	plt.plot(x,y,color = 'r', label = "line of regression")
	plt.scatter(X,Y,color = 'b', label = "Data plot")

	plt.xlabel("Head size");
	plt.ylabel("Brain size");
	
	plt.legend()
	plt.show()

	#R-Square ch calculation
	
def main():
	#print("Enter file name of dataset")
	#name = input()

	MarvellousHeadBrain("HeadBrain.csv")


if __name__ == "__main__":
	main()