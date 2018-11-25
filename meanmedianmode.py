def mean(lst):
    mean = sum(lst)/len(lst)
    return mean

def median(lst):
    median=0
    if len(lst)%2==0:
        median = (lst[int(len(lst)/2)] + lst[int(len(lst)/2)-1])/2
    else:
        median = lst[int(len(lst)/2)]
    return median

def mode(lst):
    mode = "Mode note available"
    return mode

def meanmedianmode(lst):
    print (mean(lst))
    print(median(lst))
    print (mode(lst))

a=[1,2,3,4,5,6,100]
meanmedianmode(a)
