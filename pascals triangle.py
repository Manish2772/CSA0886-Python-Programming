def get_pascals_triangle_row(rowIndex):
    row = [1] * (rowIndex + 1)
    for i in range(1, rowIndex):
        for j in range(i, 0, -1):
            row[j] += row[j - 1]
    return row

# Test Case 1
rowIndex = 3
print(get_pascals_triangle_row(rowIndex))  

# Test Case 2
rowIndex = 0
print(get_pascals_triangle_row(rowIndex))  
