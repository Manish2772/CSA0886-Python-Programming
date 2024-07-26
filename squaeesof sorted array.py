def sortedSquares(nums):
    return sorted([num**2 for num in nums])

# Test Case 1
nums1 = [-4, -1, 0, 3, 10]
print(sortedSquares(nums1))  

# Test Case 2
nums2 = [-7, -3, 2, 3, 11]
print(sortedSquares(nums2))  