def twoSum(nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        output = []
        
        for i in range(n, n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] + nums[j] == target:
                    output.append(i, j)
        return output

print(twoSum([2,7,11,15], 9))