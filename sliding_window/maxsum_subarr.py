"""
maximum sum of any cont subarray of size k
arr =[2, 1, 5, 1, 3, 2] k=3
op : [5, 1, 3]

"""
# TC : O(N) | SC : O(1)
from typing import List 
def maxsum_arr(arr:List[int], k:int) -> List[int]:
    w_sum, w_start = 0, 0
    max_len = 0
    st_idx, ed_idx =0,0 
    for w_end in range(0, len(arr)):
        w_sum += arr[w_end]
        print(w_end , " : ", k - 1)
        if w_end >= k - 1:
            if w_sum > max_len:
                max_len = w_sum
                st_idx = w_end - (k - 1)
                ed_idx = w_end + 1
            w_sum -= arr[w_start]
            w_start += 1
    return max_len , arr[st_idx : ed_idx]


print(maxsum_arr([8, 1, 1, 1, 3, 2], 3))
print(maxsum_arr([2, 1, 5, 1, 3, 2], 3))
