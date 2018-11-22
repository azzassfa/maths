def power(x,y):
    pow=1
    for i in range(1,y+1):
        pow*=x
    return pow

print (pow(2,5))
