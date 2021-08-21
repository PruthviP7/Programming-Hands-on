#Accept number from user and display all the numbers till that number.
#Input : 8
#Output : 1 2 3 4 5 6 7 8

#Input : -6
#Output : 1 2 3 4 5 6 (consider it plus number)

def DisplayNo(ino):

	if(ino < 0):
		ino = -ino 

	for i in range(1,ino+1):
		print(i,end=" ")

def main():
	iNo = int(input("Enter the number"))

	DisplayNo(iNo)

if __name__ == "__main__":
	main()