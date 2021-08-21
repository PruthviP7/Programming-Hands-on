
import numpy as np


def MarvellousRegression():
	X = [1,2,3,4,5]
	Y = [3,4,2,4,5]
	
	X_Mean = np.mean(X)	#this is X bar
	Y_Mean = np.mean(Y)	#this is Y bar

	Numerator = 0
	Denominator = 0

	for i in range(len(X)):	#5 vela firel
		Numerator = Numerator + ((X[i] - X_Mean) * (Y[i] - Y_Mean))
		Denominator = Denominator + ((X[i] - X_Mean)**2)

	m = Numerator / Denominator

	print("Values of X",X)
	print("Values of Y",Y)

	print("Value of m : ",m)

	#t = mx + c
	c = Y_Mean - (m * X_Mean)

	print("Value of C is :" ,c)

	Numerator = 0
	Denominator = 0

	for i in range(len(X)):
		Numerator = Numerator + (((m*X[i] + c) - Y_Mean)**2)
		Denominator = Denominator + ((Y[i] - Y_Mean)**2)

	RSquare = Numerator / Denominator

	print("Value of RSquare is : ",RSquare)
	

def main():
	print("__________Marvellous Regression______________")
	
	MarvellousRegression()

if __name__ == "__main__":
	main()