'''Accept number from user and calculate its power.
Input  :  2 4
Output :  2*2*2*2 = 16

Input : 4 3
Output : 4*4*4 = 64


	iNo1 5	 	iNo2 4

	5 * 5 * 5 * 5
	1 * 5 = 5 
	5 * 5 = 25
'''

def CalculatePower(ino1,ino2):
	
	iMul = 1	

	for i in range(ino2):
		iMul = iMul * ino1
	return iMul

def main():
	print("Enter first number")
	iNo1 = int(input())

	print("Enter second number")
	iNo2 = int(input())

	iRet = CalculatePower(iNo1,iNo2)
	print(f"{iNo2} times power of {iNo1} is {iRet}")

if __name__ == "__main__":
	main()