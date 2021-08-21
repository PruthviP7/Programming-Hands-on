import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def MarvellousHeadBrain(Name):
	dataset = pd.read_csv(Name)
	print("Size of our data set is",dataset.shape)

	X = dataset["HeadSize(cm^3)"].values
	Y = dataset["Brain Weight(grams)"].values
	X = X.reshape((-1,1))

	obj = LinearRegression()
	obj.fit(X,Y)

	output = obj.predict(X)
	#Dataset = pd.read_csv("Test.csv")	#fakta 4 value ghya test.csv madhe test karna sathi
	#X_new = dataset["HeadSize"].values
	#Output = obj.predict(X_new)
	#print("Expected Result is : ",output)

	rsquare = obj.score(X,Y)

	print("Value of R Square is : ",rsquare)

def main():
	#print("Enter file name of dataset")
	#name = input()

	MarvellousHeadBrain("HeadBrain.csv")


if __name__ == "__main__":
	main()