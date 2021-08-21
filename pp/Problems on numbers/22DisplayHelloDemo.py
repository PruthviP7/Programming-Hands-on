'''
Accept on number from user if number is less than 10 then print "Hello" otherwise print "Demo".  

'''
def Display(iNo):
	if iNo <= 10:
		print("Hello")
	else:
		print("Demo")

def main():
	print("Enter the number")
	iNo = int(input())

	Display(iNo)
	
if __name__ == "__main__":
	main()