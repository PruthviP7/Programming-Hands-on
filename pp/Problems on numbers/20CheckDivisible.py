'''
Accept one number and check whether is is divisible by 5 or not. 

'''

def CheckDivisible(iNo):
	if(iNo % 5 == 0):
		return True
	else:
		return False
	

def main():
	print("Enter the number")
	iNo = int(input())

	bRet = CheckDivisible(iNo)
	if(bRet == True):
		print(f"Number {iNo} is Divisible by 5")
	else:
		print(f"Number {iNo} is not Divisible by 5")

if __name__ == "__main__":
	main()