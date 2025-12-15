a = [1,2,3,4,5,9,7,8,7,9,10]

def twoSumSorted(mylist,target):
    
    mylist.sort()
    
    left = 0
    right = len(mylist)-1
    
    while left<right:
        sum = mylist[left]+mylist[right]
        if sum>target:
            right -=1
            
        if sum < target:
            left+=1
            
        if sum == target:
            return(mylist[left],mylist[right])
            
    
    print('not possible with this target')
    return

            
twoSumSorted(a, 16)
