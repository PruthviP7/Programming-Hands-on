'''
Accept number from user and check whether it is prime or not.
input - 13
output - it is prime
input - 12
output - it is not prime
'''

def CheckPrime(iNo):
	for i in range(2,iNo+1):
		if(iNo % i == 0):
			break

	if(iNo == i):
		return True
	else:
		return False
	

def main():
	print("Enter the number")
	iNo = int(input())
	
	bRet = CheckPrime(iNo)
	if(bRet == True):
		print("Number is Prime")
	else:
		print("Number is not Prime")

if __name__ == "__main__":
	main()