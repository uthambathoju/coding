import collections 
def freq(s):
    s1 = ""
    for char, times in collections.Counter(s).most_common():
        print(char * times)
        s1 += char * times
    return s1
print(freq("tree"))

