"""
find average of all contiguous subarrays of size k in it
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2] k=5
1) (1 + 3 + 2 + 6 - 1) / 5 = 2.2
2) (3 + 2 + 6 - 1 + 4) / 5 = 2.8

op : [2.2, 2.8, 2.4, 3.6, 2.8]
"""
# TC : O(N) | SC : O(1)
from typing import List
def sub_arr(arr:List[int], k : int) -> List[float]:
    w_start, w_sum = 0, 0
    res = []
    for w_end in range(0, len(arr)):
        w_sum += arr[w_end]
        if w_end >= k - 1:
            res.append(w_sum/k)
            w_sum -= arr[w_start]
            w_start += 1
    return res 

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2] 
k=5
print(sub_arr(arr, k))
