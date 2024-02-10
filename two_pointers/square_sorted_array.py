"""
Given a sorted array, create a new array containing squares of 
all the number of the input array in the sorted order.

"""

def sq_arr(arr):
    n = len(arr)
    res = [0 for x in range(n)]
    high_sq_idx = n - 1
    left_sq_idx = 0
    right_sq_idx = n - 1
    #checks left and right idx and we start assigning 
    # the last ele sqre value(since the arr is sorted) to last idx
    while left_sq_idx <=  right_sq_idx:
        left_sq = arr[left_sq_idx] * arr[left_sq_idx]
        right_sq = arr[right_sq_idx] * arr[right_sq_idx]
        # decrement the result arr from last by 1
        if left_sq < right_sq:
            res[high_sq_idx] = right_sq
            right_sq_idx -= 1
        else:
            res[high_sq_idx] = left_sq
            left_sq_idx += 1
        high_sq_idx -= 1
    return res


"""
Time complexity #
The time complexity of the above algorithm will be O(N) 
as we are iterating the input array only once.

Space complexity #
The space complexity of the above algorithm will also be O(N); 
this space will be used for the output array.
"""
    
print(sq_arr([-2, -1, 0, 2, 3]))
print(sq_arr([-3, -1, 0, 1, 2]))
