# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def permute(nums):
    def backtrack(first):
        # if all integers are used up
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            # rotate
            nums[first], nums[i] = nums[i], nums[first]
            print(("\t" * first), i, nums)
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
    
    n = len(nums)
    output = []
    backtrack(0)
    return output


print (permute([1,2,3]))


# 
# line 13:
#   i = 0
#   first = 0
#   swapping with self because i == first
#
# result = [1, ]
# 
#
# > line 13:
# >  i = 0
# >  first = 1
# >  swapping with self because i == first
# >
# > result = [1, 2, ]