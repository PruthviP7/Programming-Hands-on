'''
Program to print 5 to 1 numbers on screen.
 
'''

def Display(iNo):
	for i in range(iNo,0,-1):	
		print(i)
	

def main():
	print("Enter the number")
	iNo = int(input())

	iRet = Display(iNo)

if __name__ == "__main__":
	main()