'''
Write a program which accept one number from user and print that number of even numbers on screen.  
Input :  7  
Output:  2 4  6  8  10  12  14 

'''
def Display(iNo):
	for i in range(1,iNo+1):
		print(i * 2,end = " ")
	
def main():
	print("Enter the number")
	iNo = int(input())

	Display(iNo)
	
if __name__ == "__main__":
	main()