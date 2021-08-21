# Accept the number from the user and check whether that number is divisible by 3 and 5.

# Input:4
# Output:4 is not divisible by 3 and 5

# Input:15
# Output:15 is divisible by 3 and 5

from marvellous import CheckDivisible

def main():
	print("Enter the number")
	iNo = int(input())

	bRet = CheckDivisible(iNo)
	if(bRet == True):
		print("Number is divisible by 3 and 5")
	else:	
		print("Number is not divisible by 3 and 5")
	

if __name__ == "__main__":
	main()