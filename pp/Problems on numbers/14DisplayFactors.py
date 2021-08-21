'''
Accept number from user and display factors from that number
Input  :  12
Output :  1 2 3 4 6

Input : 20
Output : 1 2 4 5 10
'''

def DisplayFactors(iNo):

	for i in range(1,(iNo//2)+1):
		if((iNo % i) == 0):
			print(i,end=" ") 

def main():
	print("Enter the number")
	iNo = int(input())
	
	DisplayFactors(iNo)

if __name__ == "__main__":
	main()