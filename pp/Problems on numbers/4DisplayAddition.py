# Accept number from user and display the addition of all the numbers till that number.
# Input : 4
# Output : 10(1 + 2 + 3 + 4)

# Input : -6
# Output : 21 (1 + 2 + 3 + 4 + 5 + 6 (consider it plus number))

def DisplayAddition(ino):

	if(ino < 0):
		ino = -ino

	sum = 0

	for i in range(1,ino+1):
		sum = sum + i

	return sum

def main():
	print("Enter the number")
	iNo = int(input())

	iRet = DisplayAddition(iNo)
	print(f"Addition of number is{iRet}")

if __name__ == "__main__":
	main()