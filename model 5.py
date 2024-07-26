def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        
        position -= 1

    return result

# testcase = 1:
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  
# testcase = 2:
nums = [-7, 3, 2, 3, 11]
print(sortedSquares(nums))