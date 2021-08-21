import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


def MarvellousPredictor(path):
	#Step 1
	data = pd.read_csv(path)
	print("Dataset loaded successfully with the size",len(data))

	#Step 2
	#Prepare data
	Features = ["Wether","Temperature"]
	print("Feature names are ",Features)

	Whether = data.Wether #wether name should match with our csv file name
	Temperature = data.Temperature 
	Play = data.Play

	lobj = preprocessing.LabelEncoder()	#converted character value into numeric value

	WhetherX = lobj.fit_transform(Whether)
	TemperatureX = lobj.fit_transform(Temperature)
	Label = lobj.fit_transform(Play)

	print("Encoded whether is ")
	print(WhetherX)
	
	print("Encoded temperature is ")
	print(TemperatureX)
	
	features = list(zip(WhetherX,TemperatureX))
	#ex-A = [1,2,3,4,5]
	    B = [11,21,51,101,111]
	   #zip =[[1,11],[2,21],[3,51],[4,101],[5,111]] 

	#Step 3
	obj = KNeighborsClassifier(n_neighbors = 3)
	obj.fit(features,Label)

	#Step 4
	output = obj.predict([[0,2]])

	if output == 1:
		print("You can play")
	else:
		print("Don't play")
	

def main():
	print("__________Marvellous Play Predictor______________")
	print("Enter the path of file which contains dataset")
	path = input()

	MarvellousPredictor(path)

if __name__ == "__main__":
	main()