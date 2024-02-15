"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

"""

from heapq import *


def find_largest_k_nums(arr, k):
    minHeap=[]
    for i in range(k):
        heappush(minHeap, arr[i])
    
    for i in range(k, len(arr)):
        if arr[i] > minHeap[0]:
            #heappop will remove the root node i, e minimum element in the heap
            heappop(minHeap)
            heappush(minHeap, arr[i])
    return minHeap 


#print(find_largest_k_nums([3, 1, 5, 12, 2, 11], 3))
print(find_largest_k_nums([3,  5,1, 12, 2, 11], 3))
print(find_largest_k_nums([5, 12, 11, -1, 12], 3))
