"""
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target
"""

def target_sum(arr, target):
    begin = 0
    end = len(arr) - 1
    for ele in range(0, len(arr)):
        pair_sum = arr[begin] + arr[end]
        if pair_sum == target:
            return [arr[begin], arr[end]]
        elif pair_sum > target:
            end -= 1
        else:
            begin += 1

#The time complexity of the above algorithm will be O(N)
print(target_sum([1,2,3,4,6], 6))
