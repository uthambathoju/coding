"""
Given an array of points in the 2D plane, find ‘K’ closest points to the origin.

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

"""


from __future__ import print_function
from heapq import *

class Point:

    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    #used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()
    
    def distance_from_origin(self):
        #ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y) 
    
    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxHeap=[]
    #put first 'k' points in the max heap
    for i in range(k):
        heappush(maxHeap, points[i])
    

    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heappop(maxHeap)
            heappush(maxHeap, points[i])
    
    #heap has k pts closest to origin , return them as list
    return list(maxHeap)

pts=[Point(1,3), Point(3, 4), Point(2,-1)]
result = find_closest_points(pts, 2)

for pt in result:
    pt.print_point()



"""
Time complexity #
The time complexity of this algorithm is (N∗logK) as we iterating all points and pushing them into the heap.

Space complexity #
The space complexity will be O(K) because we need to store ‘K’ point in the heap.
"""
