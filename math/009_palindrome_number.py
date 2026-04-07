# 009. Palindrome Number
# Difficulty: Easy
# Topics: Math
# Time: O(log n)
# Space: O(1)

# 9. Число палиндрома
# Легко
# Темы
# Компании
# Подсказка
# Задано целое число x, верните, true если x это 
# палиндром
#  в противном случаеfalse, и .

 

# Пример 1:

# Ввод: x = 121 
# Вывод:true 
# Пояснение: 121 читается как 121 слева направо и справа налево.
# Пример 2:

# Ввод: x = -121 
# Вывод:false 
# Пояснение: Слева направо написано -121. Справа налево он становится 121-. Следовательно, это не палиндром.
# Пример 3:

# Ввод: x = 10 
# Вывод:false 
# Объяснение: Читается 01 справа налево. Следовательно, это не палиндром.
 

# Ограничения:

# -231 <= x <= 231 - 1
 

# Продолжение: Не могли бы вы решить задачу, не преобразовывая целое число в строку?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]

        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        rev = 0
        while x > rev:

            rev = rev * 10 + x % 10
            x = x // 10
            print(x, rev)
        return x == rev or x == rev // 10


solution = Solution()
print(solution.isPalindrome(1221))