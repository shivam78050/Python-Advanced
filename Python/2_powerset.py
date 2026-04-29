def power_set(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    
    backtrack(0, [])
    return result
# Example usage
input_nums = [1, 2, 3]
print(power_set(input_nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]  

