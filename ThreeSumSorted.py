def threeSumSorted(mylist, target):
    mylist.sort()
    result = []
    
    
    for i in range(len(mylist)-2):
        
        if i>0 and mylist[i]==mylist[i-1]:
            continue
        
        newtarget= target- mylist[i]
        
        left = i+1
        right = len(mylist)-1
        
        
        while left<right:
            sum = mylist[left]+mylist[right]
            
            if sum<newtarget:
                left +=1
                
            elif sum>newtarget:
                right -=1
                
            elif sum == newtarget:
                result.append([mylist[i],mylist[left],mylist[right]])
                
                while left<right and mylist[left]==mylist[left+1]:
                    left +=1
                    
                while left<right and mylist[right] == mylist[right-1]:
                    right -=1
                    
                left +=1
                right-=1
                
    return result

print(threeSumSorted([-1, 0, 1, 2, -1, -4], 0))
# Expected: [[-1, -1, 2], [-1, 0, 1]]

print(threeSumSorted([1, 2, 3, 4, 5], 10))
# Expected: [[[1, 4, 5], [2, 3, 5]]]

print(threeSumSorted([-5, -3, -2, 0, 1, 3], -5))
# Expected: [[-5, 0, 0], [-3, -2, 0]] 
