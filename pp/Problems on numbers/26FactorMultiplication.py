'''
Write a program which accept number from user and display its multiplication of factors. 
Input :  12 Output : 144  (1 * 2 * 3 * 4 * 6) 
Input : 13 Output : 1  (1) 
Input :  10   Output : 10  (1 * 2 * 5)

'''
def MultFact(iNo):
	iMul = 1;
	for i in range(1,iNo+1//2):
		if((iNo % i) == 0): 
			iMul = iMul * i;

	return iMul;
	
	
def main():
	print("Enter the number");
	iNo = int(input());

	iRet = MultFact(iNo)
	print(f"Factor Multiplication of number {iNo} is {iRet}");

if __name__ == "__main__":
	main()