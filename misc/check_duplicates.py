from collections import defaultdict
def contains_duplicate(arr):
    dupl_dict = defaultdict(int)
    for num in arr:
        dupl_dict[num] = 1 + dupl_dict.get(num, 0)
        if dupl_dict.get(num) > 1:
            return True
    return False 

print(contains_duplicate([1, 2, 3, 1]))
