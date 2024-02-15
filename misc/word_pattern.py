def check_pattern(p, s):
    pt_dict = {}
    s_arr = s.split(" ")
    for i in range(0, len(p)):
        char = p[i]
        if char in pt_dict:
            if pt_dict.get(char) != s_arr[i]:
                return False 
        else:    
            pt_dict[char] = s_arr[i]
    return True 

print(check_pattern("abba", "dog cat cat dog"))
print(check_pattern("abba", "dog cat cat fish"))
print(check_pattern("aaaa", "dog cat cat dog"))
