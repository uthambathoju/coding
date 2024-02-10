"""
find length of smallest contiguous subarray whose sum is greater than or equal to s
return 0 if no such subarray exists
arr = [2, 1, 5, 2, 3, 2], s=7
op : 2
the smallest sub array with a sum greater than or equal to 7 is [5, 2]

arr = [2, 1, 5, 2, 8], s=7
op:1
the smallest sub array with a sum greater than or equal to 7 is [8]
"""
import math
def smallest_subarr(arr, s):
    w_start , res, w_sum  = 0, math.inf, 0 
    for w_end in range(0, len(arr)):
        w_sum += arr[w_end]
        while w_sum >= s:
            res = min(res, w_end - w_start + 1)
            w_sum -= arr[w_start]
            w_start += 1
    return res

print(smallest_subarr([2, 1, 5, 2, 8], 7))
print(smallest_subarr([2, 1, 5, 2, 3, 2], 7))
"""
TC will be O(N).outer for loop runs for all elements and inner while loop
processes each element only once.so TC will be O(N + N) which is
asymptotically equvialent to O(N)

SC : O(1)
"""

