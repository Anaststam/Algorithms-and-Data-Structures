"""
# Created by anastasia on 1/8/20
"""

#exception handling
#logging

class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:

            print('User provided positive number')
            string_num = str(x)
            reversed_string= []
            index = len(string_num) - 1
            index2 = len(string_num) - 1
            while index >= 0:
                reversed_string.insert(index2-index, string_num[index])
                index = index-1
            res = int("".join(reversed_string))
            if res >= (-2**31) and res <= (2**31 -1 ):

                return (res)
            else:
                print('Overflow')
                return(0)

        else:
            print('User provided negative number')
            string_num = str(x)
            reversed_string = []
            index = len(string_num) - 1
            index2 = len(string_num) - 1
            while index > 0:
                reversed_string.insert(index2 - index, string_num[index])
                index = index - 1
            reversed_string.insert(0, "-")
            res = int("".join(reversed_string))
            if res >= (-2**31) and res <= (2**31 -1 ):
                return (res)
            else:
                print('Overflow')
                return (0)

solution = Solution()

reversed_integer = solution.reverse(x = 0)
print(reversed_integer)