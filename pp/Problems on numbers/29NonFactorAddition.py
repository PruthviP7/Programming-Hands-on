'''
4.Write a program which accept number from user and return summation of all its non factors. 
Input :  12 Output : 50  
Input :  10  Output : 37 

'''

def NonFactorAdditon(ino):
    iSum = 0;
    for i in range(2,ino):
        if ((ino % i)!=0):
            iSum = iSum + i;

    return iSum;

def main():
    iNo = int(input("Enter the number"));

    iRet = NonFactorAdditon(iNo);
    print(f"Nonfactor Addition of number {iNo} is {iRet}");


if __name__ == "__main__":
    main()