def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

def factorialRecursive(num):
    if num==1:
        return 1
    else:
        return num*factorialRecursive(num-1)


print (factorial(5))
print (factorialRecursive(10))
