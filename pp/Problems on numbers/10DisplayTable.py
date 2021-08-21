'''Accept number from user and display its  table
   Input 4
   output 4 8 12 16 20 24 28 32 36 40

	Input 5

	5 * 1 	5
	5 * 2	10
	5 * 3	15
	5 * 4	20	iNo	      5
	5 * 5	25	Common        5 * ____
	5 * 6	30	Start	      1
	5 * 7	35	End	      10
	5 * 8	40	Displacement  1
	5 * 9	45
	5 * 10	50
'''

def DisplayTable(ino):
	
	for i in range(1,11):
		#print(str(ino)+" * "+str(i)+" = " ,ino*i)

		#print(f"{ino} * {i} = ",ino*i)		#using f string
		print(f"{ino} * {i} = {ino*i}")		#using f string


def main():
	print("Which table you want to see")
	iNo = int(input())

	DisplayTable(iNo)

if __name__ == "__main__":
	main()