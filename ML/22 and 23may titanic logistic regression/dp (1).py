import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show 
from seaborn import countplot

def TitanicLogistic():
	print("Inside TitanicLogistic Function")	

	#Step 1-Load Data

	titanic_data=pd.read_csv("titanic.csv")

	print("First Five records of Dataset:")
	
	print(titanic_data.head())

	print("Total number of records are:",len(titanic_data))	#.info

	
	#Step 2-Analyse the data
	
	print("Vizualization of Survived and non-survived Passengers")

	figure()
		
	countplot(data=titanic_data, x="Survived").set_title("Non-Survived vs Survived")

	show()

	print("Vizualition according to the Gender:")
	
	figure()
	
	countplot(data=titanic_data, x="Survived",hue="Sex").set_title("Ex:Male vs Female")

	show()

	print("Vizualition according to the Passenger Class:")
	
	figure()
	
	countplot(data=titanic_data, x="Survived",hue="Pclass").set_title("Non-Survived vs Survived:Pclass")

	show()


	print("Survived vs Non-Survived Based on Age")

	figure()
	
	titanic_data["Age"].plot.hist().set_title("Non-Survived vs Survived:Age")

	show()	

	#step 3-Data Cleaning
	
	titanic_data.drop("zero",axis=1,inplace=True)

	print("The data after column removal is:")

	print(titanic_data.head())

	Sex=pd.get_dummies(titanic_data["Sex"])

	print(Sex.head())

	Sex=pd.get_dummies(titanic_data["Sex"],drop_first=True)

	print("Sex Column after Updation:")
	
	print(Sex.head())

	Pclass=pd.get_dummies(titanic_data["Pclass"])

	print(Pclass.head())

def main():
	print("Logistic Case Study..Titanic Survival")	
	
	TitanicLogistic()	


if __name__=="__main__":
	main()