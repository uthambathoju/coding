"""
Two baskets are given and we need to get longest sequence where max fruits can be filled.
each basket can contain only one fruit
Input : fruit=['A', 'B', 'C', 'A', 'C']
output : 3
"""

def fill_baskets(arr):
    max_fruits, max_w_st,  w_start, fruit_freq = 0, 0, 0, {}
    for w_end in range(0, len(arr)):
        fruit = arr[w_end]
        fruit_freq[fruit] = 1 + fruit_freq.get(fruit, 0)
        if len(fruit_freq) > 2:
            init_char = arr[w_start] 
            fruit_freq[init_char] -= 1
            if fruit_freq[init_char] == 0:
                fruit_freq.pop(init_char)
            w_start += 1
        if w_end - w_start + 1 > max_fruits:
                max_fruits = w_end - w_start + 1
                max_w_st = w_start
    return max_fruits, arr[max_w_st:max_w_st + max_fruits]

"""
TC: outer for loop runs for all chars and inner while loop processes each character only once, 
O(N + N) which is asymptotically equivalent to O(N)

SC: O(1)
"""
print(fill_baskets(['A','B','C','A','C']))
print(fill_baskets(['A','B','C','B','B','C']))
