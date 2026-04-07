# 001. Two Sum
# Difficulty: Easy
# Topics: Array, Hash Table
# Time: O(n)
# Space: O(n)

# Idea:
# Use a hash map (dictionary) to store numbers we've seen.
# For each number, check if its complement exists in the map.

# Идея:
# Используем словарь т
# 
#  для хранения уже просмотренных чисел.
# Для каждого числа ищем (target - num) в словаре.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], index]

            num_dict[num] = index


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))