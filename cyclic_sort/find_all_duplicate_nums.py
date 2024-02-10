"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
find all the duplicate numbers without using any extra space.

"""

# TC O(N) | SC O(1)
def dupl_num(arr):
    i = 0
    n =len(arr)
    while i < n:
        j = arr[i] - 1
        print(arr[i], arr[j])
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    res = []
    for k in range(1, len(arr)):
        if k != arr[k-1]:
            res.append(arr[k])
    return res



print(dupl_num([3, 4, 4, 5, 5]))
print(dupl_num([5, 4, 7, 2, 3, 5, 3]))
