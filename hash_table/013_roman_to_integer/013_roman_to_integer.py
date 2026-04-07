# 013. Roman to Integer
# Difficulty: Easy
# Topics: Hash Table, Math, String
# Time: O(n)
# Space: O(1)

# Idea:
# Traverse the string from left to right.
# Compare the current symbol with the next one.
# If the current value is smaller than the next, subtract it.
# Otherwise, add it to the result.
# After the loop, add the value of the last symbol.

# Идея:
# Проходим по строке слева направо.
# Сравниваем текущий символ со следующим.
# Если текущее значение меньше следующего, вычитаем его.
# Иначе прибавляем к результату.
# После цикла добавляем значение последнего символа.

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_rim = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        num = 0

        for index in range(len(s) - 1):
            if dict_rim.get(s[index]) < dict_rim.get(s[index+1]):
                num -= dict_rim.get(s[index])
            else:
                num += dict_rim.get(s[index])

        num += dict_rim[s[-1]]
                
        return num
        
if __name__ == "__main__":
    print(Solution().romanToInt('MCMXCIV'))