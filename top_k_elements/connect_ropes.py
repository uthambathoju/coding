"""
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
The cost of connecting two ropes is equal to the sum of their lengths.
Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
"""


"""
Solution #
In this problem, following a greedy approach to connect the smallest ropes first will ensure the lowest cost. 
We can use a Min Heap to find the smallest ropes following a similar approach as discussed in Kth Smallest Number. 
Once we connect two ropes, we need to insert the resultant rope back in the Min Heap so that we can connect it with the remaining ropes.
"""

from heapq import * 

def min_cost_to_cnect_ropes(ropes_len):
    minHeap = []
    #add all ropes to min heap
    for i in ropes_len:
        heappush(minHeap, i)

    #go through the values of heap , in each step take top(lowest) rope lengths from min heap
    # connect them and push result back to min heap
    # keep doing this until the heap is left with only one rope

    result, temp =0, 0
    while len(minHeap) > 1:
        temp = heappop(minHeap) + heappop(minHeap)
        result += temp 
        heappush(minHeap, temp)

    return result


print("Min cost to connect ropes :: ", str(min_cost_to_cnect_ropes([1, 3, 11, 5])))
print("Min cost to connect ropes :: ", str(min_cost_to_cnect_ropes([3, 4, 5, 6])))


"""
Time complexity #
Given ‘N’ ropes, we need O(N∗logN) to insert all the ropes in the heap. In each step, while processing the heap, we take out two elements 
from the heap and insert one. This means we will have a total of ‘N’ steps, having a total time complexity of  O(N∗logN).

Space complexity #
The space complexity will be  O(N) because we need to store all the ropes in the heap.
"""
