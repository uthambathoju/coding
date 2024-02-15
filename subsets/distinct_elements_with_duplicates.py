"""
Given a set with distinct elements, find all of its distinct subsets.
Input: [1, 3]
Output: [], [1], [3], [1,3]
"""

def find_subsets(nums):
    nums.sort()
    subsets = []
    #create empty subset
    subsets.append([])
    startIndex, endIndex =0, 0
    for i in range(len(nums)):
        startIndex = 0
        #if cur and prev elements are same , create only the subsets added from the prev step
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        # we decrement 1 be'coz if current and prev ele are same in the if condition then
        # to get the right set of ele's added in prev index as start index we do it , if we 
        # dont decrement then we'll miss the first subset added in prev step
        endIndex = len(subsets) - 1
        # in for loop we append 1 again to iterate on all the subsets added in prev step
        for j in range(startIndex, endIndex + 1):
            #get the previously added subsets(line num 18) and append current number
            existingSubset = list(subsets[j])
            existingSubset.append(nums[i])
            subsets.append(existingSubset)
    return subsets


print(find_subsets([1,3,3]))
print(find_subsets([1,5,3,3]))

"""
Time complexity #
Since, in each step, the number of subsets could double (if not duplicate) as we add each element to all the existing subsets, the time complexity of the above algorithm is 
�
(
2
�
)
O(2
​N
​​ ), where ‘N’ is the total number of elements in the input set. This also means that, in the end, we will have a total of 
�
(
2
�
)
O(2
​N
​​ ) subsets at the most.

Space complexity #
All the additional space used by our algorithm is for the output list. Since at most we will have a total of 
�
(
2
�
)
O(2
​N
​​ ) subsets, the space complexity of our algorithm is also 
�
(
2
�
)
O(2
​N
​​ ).
"""
