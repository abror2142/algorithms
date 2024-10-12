def canSumOptimized(target, array, memo={}):
    if target in memo: 
        return memo[target]
    
    if target == 0:
        return True
    
    if(target < 0):
        return False
    
    for num in array:
        if(canSumOptimized(target-num, array, memo)):
            memo[target] = True
            return True
        
    memo[target] = False
    return False
    

def canSumNaive(target, array):
    if target == 0:
        return True

    if target < 0:
        return False

    for num in array:
        if(canSumNaive(target-num, array)):
            return True
        
    return False


print(canSumOptimized(20, [7, 3]))
print(canSumNaive(2000, [7, 13, 3, 4, 5, 6, 10, 9]))
    