def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Test cases
test_case_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_case_2 = [[1, 2], [3, 4], [5, 6]]

print(f"Input: {test_case_1} -> Output: {transpose(test_case_1)}")
print(f"Input: {test_case_2} -> Output: {transpose(test_case_2)}")
