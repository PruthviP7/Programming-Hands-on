""" 
  0 to 35 - fail
  35 to 50 - pass class
  50 to 60 - second class
  60 to 70 - first class
  70 to 100 - Distinction
"""


def CheckResult(iMarks):
	if((iMarks < 0) or (iMarks > 100)):
		print("Enter Valid Marks")
		return

	if(iMarks>= 0 and iMarks < 35):
		print("You are Fail")

	elif(iMarks >= 35 and iMarks < 50):
		print("You Got Pass class")

	elif(iMarks >= 50 and iMarks < 60):
		print("You got second class")
	
	elif(iMarks >= 60 and iMarks < 70):
		print("You got first class")

	else:
		print("Congrats!!! You got Distinction")

def main():
	print("Enter your marks")
	iMarks = float(input())

	CheckResult(iMarks)

if __name__ == "__main__":
	main()