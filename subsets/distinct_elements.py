"""
Given a set with distinct elements, find all of its distinct subsets.
Input: [1, 3]
Output: [], [1], [3], [1,3]
"""

def find_subsets(nums):
    subsets = []
    #create empty subset
    subsets.append([])
    for currentNumber in nums:
        #take all existing subsets and insert current number to create new subsets and add to subsets list
        n = len(subsets)
        for i in range(n):
            #get the previously added subsets(line num 18) and append current number
            existingSubset = list(subsets[i])
            existingSubset.append(currentNumber)
            subsets.append(existingSubset)
    return subsets


print(find_subsets([1,3]))
print(find_subsets([1,5,3]))
