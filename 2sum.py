# Two sum - array is sorted  
# input - array, target - return indices of the two numbers that add up to target
# one unique solution

# array = [2, 3, 5, 7]
# target = 8
# 
# i = 0
# j = len(array)-1
# 
# [2, 3, 5, 7]
#  ^        ^
# 9 > 8
# 
# 

# [2, 3, 3, 4, 6, 7, 8, 8, 10]
#     ^           ^
# target = 11
# 
# i = 0
# j = len(array) - 1
#
# 12
# 
# []
# [1, 5],
# [2, 5],
# 


def test(array, target):
    result = []
    i = 0
    j = len(array) - 1
    while i < j:
        if i > 0 and array[i] == array[i-1]:
            i += 1
            continue

        total = array[i] + array[j]
        if total > target:
            j -= 1
        elif total < target:
            i += 1
        else:
            result.append([i, j])
            i += 1
            # j -= 1
    return result



