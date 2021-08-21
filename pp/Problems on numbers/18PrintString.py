'''
Program to print 5 times "Marvellous" on screen.  
 
'''

def Display(iNo):
	for i in range(iNo):
		print("Marvellous")	
	

def main():
	print("Enter the number")
	iNo = int(input())

	iRet = Display(iNo)

if __name__ == "__main__":
	main()