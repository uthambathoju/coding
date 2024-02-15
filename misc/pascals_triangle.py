"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]

"""

def pascals(num_rows):
    res =[[1]]
    for _ in range(1, num_rows):
        m = [0] + res[-1] + [0]
        row = []
        for j in range(0, len(m) - 1):
            val = m[j] + m[j + 1]
            row.append(val)
        res.append(row)
    return res 

print(pascals(5))
print(pascals(1))
