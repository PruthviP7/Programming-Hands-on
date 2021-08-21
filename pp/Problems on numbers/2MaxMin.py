#Accept 2 numbers from user and return the maximum and minimum number

from marvellous import MaxMin

def main():
	print("Enter first number")
	iNo1 = int(input())		

	print("Enter second number")
	iNo2 = int(input())	

	iRet = MaxMin(iNo1,iNo2)

	print("Maximum number is ",iRet)
	

if __name__ == "__main__":
	main()