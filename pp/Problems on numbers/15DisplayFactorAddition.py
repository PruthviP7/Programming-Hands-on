'''
Accept number and return the addition of its factors
Input  :  6
Output :  1 + 2 + 3

Input : 12
Output : 1 + 2 + 3 + 4 + 6 = 16
'''

def FactorAddition(iNo):
	iSum = 0
	for i in range(1,(iNo//2)+1):
		if((iNo % i) == 0):
			iSum = iSum + i
	return iSum

def main():
	print("Enter the number")
	iNo = int(input())
	
	iRet = FactorAddition(iNo)
	print("Factor Additon of {0} is {1}".format(iNo,iRet))

if __name__ == "__main__":
	main()