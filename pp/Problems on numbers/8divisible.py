"""
	Input : 15 5
	Output : 15 is divisible by 5

	Input : 21 6
	Output : False
"""

def CheckDivisible(ino1,ino2):
	if(ino1 % ino2 == 0):
		return True
	else:
		return False

def main():

	print("Enter first number")
	iNo1 = int(input())

	print("Enter second number")
	iNo2 = int(input())

	bRet = CheckDivisible(iNo1,iNo2)
	if(bRet == True):
		print(f"{iNo1} is divisible by {iNo2}")
	else:	
		print(f"{iNo1} is not divisible by {iNo2}")
	
	
if __name__ == "__main__":
	main()