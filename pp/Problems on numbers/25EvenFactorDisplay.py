'''
Write a program which accept number from user and print even factors of that number.  
Input :  24 
Output:  1 2 4 6 8 12 

'''
def Display(iNo):
	for i in range(1,(iNo//2)+1):
		if((iNo % i == 0) and (i % 2 == 0)):
			print(i,end = " ")
	
def main():
	print("Enter the number")
	iNo = int(input())

	Display(iNo)
	
if __name__ == "__main__":
	main()