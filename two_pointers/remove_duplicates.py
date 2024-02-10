"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the new length of the array.
"""
# TC O(N) | SC O(1)
def remove_duplicates(arr):
    non_duplicate = 1
    i = 1
    while(i < len(arr)):
        if arr[non_duplicate - 1] != arr[i]:
            arr[non_duplicate] = arr[i]
            non_duplicate += 1
        i += 1
    return non_duplicate


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))
