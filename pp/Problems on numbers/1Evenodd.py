#Problems of numbers

#Accept the number from the user and check whether that number is even or odd.

#Input:4
#Output:Its even

#Input:7
#Output:Its odd


def CheckEven(iNo):
	if((iNo % 2)==0):
		return True
	else:
		return False

def main():
	no = int(input("Enter the number"))

	bret = CheckEven(no)
	if(bret == True):
		print("Number is even")

	else:
		print("Number is odd")
	

if __name__ == "__main__":
	main()