'''
Accept number from user and return its factorial(Using while Loop)
Input  :  5
Output :  5*4*3*2*1 = 120

Input : 4 
Output : 4*3*2*1 = 24
'''

def Factorial(iNo):
	iMul = i = 1
	#i = 1

	while(i <= iNo):
		iMul = iMul * i
		i += 1
	
	return iMul


def main():
	print("Enter the number of which factorial you want")
	iNo = int(input())
	
	iRet = Factorial(iNo)

	print(f"Factorial of {iNo} is {iRet}")

if __name__ == "__main__":
	main()