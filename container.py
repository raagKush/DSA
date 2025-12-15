def maxVol(height): 
    max = 0
    for j in range(len(height)):
        for k in range(0, len(height)):
            # print(j,k)
            # print(j,height[j],k+1)
            if ((height[j]<=height[k]) and (j!=k)):
                # print(height[j]*abs(k-j))
                if (height[j]*abs(k-j)) >= max:
                    max = (height[j]*abs(k-j))
    return max

height = [4, 3, 100, 2, 1]
containerMaxVol = maxVol(height)
