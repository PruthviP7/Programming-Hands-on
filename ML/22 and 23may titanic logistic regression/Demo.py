#Titanic case study using Logistic Regression 

import numpy as np
import pandas as pd
import seaborn as sb
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show

def TitanicLogistic():

#Step 1)- Load Data
	Titanic_Data = pd.read_csv('MarvellousTitanicDataset.csv')
	
	print("First Five records of the Dataset")
	print(Titanic_Data.head(5))	#displayed first 5 records
	print("Total number of records are",len(Titanic_Data))

#Step 2)-Analyse the Data
	print("**********************************************************")
	print("Visualisation of Survived and non survived passengers")

	figure()	#step1) RAM tayari kar
	countplot(data = Titanic_Data,x = "Survived").set_title("Survived v\s Non-Survived")	#step 2)konta graph pahije
	show()	#step 3)RAM dakhav
	
	print("**********************************************************")
	print("Visualisation Accorging to gender or sex")

	figure()	#step1
	countplot(data = Titanic_Data,x = "Survived",hue = "Sex").set_title("Visualisation according to sex")	#step2
	show()	#step3

	print("**********************************************************")
	print("Visualisation Accorging to Passenger Class")

	figure()	#step1
	countplot(data = Titanic_Data,x = "Survived",hue = "Pclass").set_title("Visualisation according to Passenger class")	#step2
	show()	#step3

	print("**********************************************************")
	print("Survived v/s non-Survived Based on age")
	figure()
	Titanic_Data["Age"].plot.hist().set_title("Visualisation according to age")
	show()

#Step3) - Data cleaning
	Titanic_Data.drop("zero",axis = 1,inplace = True)
	print("Data after column removal")
	print(Titanic_Data.head())

	Sex = pd.get_dummies(Titanic_Data["Sex"])	#yachi itki garaj navti..pn siranni samjava mhanun ghetla a ek new topic(Data wrangling)
	print(Sex.head())

	Sex = pd.get_dummies(Titanic_Data["Sex"],drop_first = True)
	print("Sex column after updation")
	print(Sex.head())

	Pclass = pd.get_dummies(Titanic_Data["Pclass"])
	print(Pclass.head())

	#Concat Sex and Pclass field in our dataset

	Titanic_Data = pd.concat([Titanic_Data,Sex,Pclass],axis = 1)
	print("Data After concatination :")
	print(Titanic_Data.head())

	#Removing unnecessary fields
	Titanic_Data.drop(["Sex","sibsp","Parch","Embarked"],axis = 1,inplace = True)	#inplace mhanje copy nahi tayar karaychi a...tyatch update kara changes
	print(Titanic_Data.head())

def main():
	print("Case Study for titanic case study")

	TitanicLogistic()

if __name__ == "__main__":
	main()