'''
5.Write a program which accept number from user and return difference between summation of all its factors and non factors. 
Input :  12 Output : -34  (16 - 50)  
Input :  10  Output : -29 (8 - 37)  

'''

def NonFactorAdditon(ino):
    iSumF = 0;
    iSumNF = 0;
    for i in range(1,ino):
        if ((ino % i)!=0):
            iSumNF = iSumNF + i;

        else:
            iSumF = iSumF + i;    

    return iSumF - iSumNF;

def main():
    iNo = int(input("Enter the number"));

    iRet = NonFactorAdditon(iNo);
    print(f"Difference between Factor and Nonfactor of number {iNo} is {iRet}");


if __name__ == "__main__":
    main()