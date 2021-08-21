'''
//Program to divide two numbers.
 
'''

def DivideNumber(iNo1,iNo2):
	return iNo1//iNo2	
	

def main():
	print("Enter first number")
	iNo1 = int(input())

	print("Enter second number")
	iNo2 = int(input())
	
	iRet = DivideNumber(iNo1,iNo2)

	print(f"{iNo1}/{iNo2} = {iRet}")
	
if __name__ == "__main__":
	main()