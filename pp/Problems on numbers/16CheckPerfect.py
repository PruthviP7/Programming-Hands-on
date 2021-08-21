'''
Accept number  from user and check whether that perfect number or not
Accept number from user and check whether it is perfect or not
Input  :  6
Output : True(6) 1 + 2 + 3

Input : 12
Output : False(16) 1 + 2 + 3 + 4 + 6 = 16

'''

def CheckPerfect(iNo):
	iSum = 0
	for i in range(1,(iNo//2)+1):
		if((iNo % i) == 0):
			iSum = iSum + i
	if(iSum == iNo):
		return True
	else:
		return False

def main():
	print("Enter the number")
	iNo = int(input())
	
	bRet = CheckPerfect(iNo)
	if(bRet == True):
		print("Number is Perfect")
	else:
		print("Number is not Perfect")

if __name__ == "__main__":
	main()