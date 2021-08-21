'''
Accept one number from user and print that number of * on screen

'''

def DisplayStar(iNo):
	for i in range(iNo):
		print("*",end = " ")

def main():
	print("Enter the number")
	iNo = int(input())

	DisplayStar(iNo)
	
if __name__ == "__main__":
	main()