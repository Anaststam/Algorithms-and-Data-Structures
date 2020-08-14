"""
# Created by Anastasia on 1/8/20
"""
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class Solution:
    def reverse(self, x: int) -> int:

        if type(x) is not int:
            raise TypeError("Only integers are allowed")

        if x >= 0:

            logging.info('User provided non negative number')
            string_num = str(x)
            reversed_string = []
            index = len(string_num) - 1
            index2 = len(string_num) - 1
            while index >= 0:
                reversed_string.insert(index2 - index, string_num[index])
                index = index - 1
            res = int("".join(reversed_string))
            if res >= (-2 ** 31) and res <= (2 ** 31 - 1):

                return (res)
            else:
                logging.info('Overflow')
                return (0)

        else:
            logging.info('User provided negative number')
            string_num = str(x)
            reversed_string = []
            index = len(string_num) - 1
            index2 = len(string_num) - 1
            while index > 0:
                reversed_string.insert(index2 - index, string_num[index])
                index = index - 1
            reversed_string.insert(0, "-")
            res = int("".join(reversed_string))
            if res >= (-2 ** 31) and res <= (2 ** 31 - 1):
                return (res)
            else:
                logging.info('Overflow')
                return (0)

solution = Solution()

reversed_integer = solution.reverse(x = 0)
print(reversed_integer)