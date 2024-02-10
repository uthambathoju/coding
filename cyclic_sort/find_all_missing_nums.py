"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. 
Find all those missing numbers.
"""

def swap(replace_idx, current_index, arr):
    arr[replace_idx- 1], arr[current_index] = arr[current_index], arr[replace_idx- 1]

def find_missing_number(arr):
    i, n = 0, len(arr)
    while i < n:
        j = arr[i]-1
        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    missing_idx=[]
    for i in range(len(arr)-1):
        if i+1 != arr[i]:
            missing_idx.append(i+1)
    return missing_idx


#print(find_missing_number([3, 0, 1]))
print(find_missing_number([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_missing_number([2,4,1,2]))


"""
Time complexity #

The time complexity of the above algorithm is O(n). In the while loop, 
although we are not incrementing the index i when swapping the numbers, 
this will result in more than ‘n’ iterations of the loop, but in the worst-case scenario, 
the while loop will swap a total of ‘n-1’ numbers and once a number is at its correct index,
 we will move on to the next number by incrementing i. In the end, we iterate the input array again 
 to find the first number missing from its index, so overall, our algorithm will take 
O(n)+O(n−1)+O(n) which is asymptotically equivalent to O(n).

Space complexity #
The algorithm runs in constant space O(1).

"""
