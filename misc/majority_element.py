"""
#https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
#Boyer moore's voting algorithm
def majority_ele(arr) -> int:
    """
    :param arr: List
    :return: majority ele
    """
    #counter variable to cancel out on different numbers
    candidate, cnt  = 0, 0
    for ele in arr:
        #if cnt reaches zero, change the candidate to current element
        if cnt == 0:
            candidate = ele
        
        if ele == candidate:
            #increment cnt variable, when current and adj elements are same
            cnt += 1
        else:
            #decrement cnt variable, when curr and adj are different
            cnt -= 1
    return candidate

#TC : O(N) - travers through the array once
#SC : O(1) - constant variables used
print(majority_ele([3,2,3, 2, 2, 2]))
print(majority_ele([2,2,1,1,1,2,2]))
