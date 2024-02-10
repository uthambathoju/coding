"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

"""

# TC O(N) | SC O(1)
def dupl_num(arr):
    i = 0
    n =len(arr)
    while i < n:
        if arr[i] != i + 1:
            j = arr[i] - 1
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                return arr[i]
        else:
            i += 1

    return -1



print(dupl_num([1, 4, 4, 3, 2]))
print(dupl_num([2, 1, 3, 3, 5, 4]))
print(dupl_num([2, 4, 1, 4, 4]))
