"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

"""

from heapq import *

def find_kth_smallest_num(nums, k):
    maxHeap = []
    #using negative sign so that we can do integer comparsion and store top K smallest values in minheap  
    for i in range(k):
        print(-nums[i])
        heappush(maxHeap, -nums[i])

    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    return -maxHeap[0]



print("kth smallest num : ", str(find_kth_smallest_num([1, 5, 12, 2, 11, 5], 3)))
print("kth smallest num : ", str(find_kth_smallest_num([1, 5, 12, 2, 11, 5], 4)))
print("kth smallest num : ", str(find_kth_smallest_num([5, 12, 11, -1, 12], 3)))

"""
Time complexity #
The time complexity of this algorithm is 
�
(
�
∗
�
�
�
�
+
(
�
−
�
)
∗
�
�
�
�
)
O(K∗logK+(N−K)∗logK), which is asymptotically equal to 
�
(
�
∗
�
�
�
�
)
O(N∗logK)

Space complexity #
The space complexity will be 
�
(
�
)
O(K) because we need to store ‘K’ smallest numbers in the heap.

An Alternate Approach #
Alternatively, we can use a Min Heap to find the Kth smallest number. We can insert all the numbers in the min-heap and then extract the top ‘K’ numbers from the heap to find the Kth smallest number. Initializing the min-heap with all numbers will take 
�
(
�
)
O(N) and extracting ‘K’ numbers will take 
�
(
�
�
�
�
�
)
O(KlogN). Overall, the time complexity of this algorithm will be 
�
(
�
+
�
�
�
�
�
)
O(N+KlogN) and the space complexity will be 
�
(
�
)
O(N).

"""
