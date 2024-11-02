def factocial(n):
    if(n==1 or n==0):
        return 1
    return n * factocial(n-1)


n = int(input("Enter a Number: "))
print(f"The factorial of number is: {factocial(n)}")