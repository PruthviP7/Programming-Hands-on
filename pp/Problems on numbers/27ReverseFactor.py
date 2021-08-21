'''
2.Write a program which accept number from user and display its factors in decreasing order. 
Input :  12 Output : 6 4 3 2 1 
Input : 13 Output : 1  
Input :  10  Output : 5 2 1 

'''

def FactorReverse(ino):
    for i in range(ino//2,0,-1):
        if ((ino % i)==0):
            print(i,end=" ")

def main():
    iNo = int(input("Enter the number"));

    FactorReverse(iNo)


if __name__ == "__main__":
    main()