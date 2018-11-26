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

    # initialize 2 arrays one for numbers and one for occurences
    nums=[]
    occurences = []
    found =0
    mode=0
    modeCount=0

    for i in range(len(lst)):                   # run a loop for items in lst
        for j in range(len(occurences)):        # run another loop for checking occurence in occurences array
            if lst[i] == nums[j]:
                found=1                         # if found, increase count and set flag
                nums[j] = lst[i]
                occurences[j]+=1
                if occurences[j] > modeCount:   # check which element is mode
                    modeCount=occurences[j]
                    mode=nums[j]
        if found == 0:                            # when loops end if flag not fooung add entry
            nums.append(lst[i])
            occurences.append(1)
            if 1 > modeCount:
                modeCount=1
                mode=lst[i]

    return mode

    mode = "Mode note available"
    return mode

def meanmedianmode(lst):
    print (mean(lst))
    print(median(lst))
    print (mode(lst))

a=[2,4,6,8,10,2]
meanmedianmode(a)
