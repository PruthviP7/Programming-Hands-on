'''
Input :  12 5 
Output : 12 12 12 12 12 
Input : -2 3 
Output : -2 -2 -2  
Input :  21 -3 
Output : 21 21 21  
Input :  -2 0 
Output :  

'''
def Display(iNo1,iNo2):
	for i in range(iNo2):
		print(iNo1,end = " ")
	
def main():
	print("Enter first number")
	iNo1 = int(input())

	print("Enter second number")
	iNo2 = int(input())

	Display(iNo1,iNo2)
	
if __name__ == "__main__":
	main()