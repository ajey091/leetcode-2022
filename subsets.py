# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. 
# Return the solution in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


def subsets(nums):
    def backtrack(first, curr = []):
        # if all integers are used up
        # if first == n:  
        if len(curr) == k:
            output.append(curr[:])
        for i in range(first, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
    
    n = len(nums)
    output = []
    for k in range(0, n+1):
        backtrack(0)
    return output


print (subsets([1,2,3]))
