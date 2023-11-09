#1 Pytest

# import pytest

# def is_negative(n1):
#     return n1 < 0
#
# def test_negative_number():
#     n2 = -3
#     assert is_negative(n2) == True
#
# def test_non_negative_number():
#     n3 = 7
#     assert is_negative(n3) == False

#2 Pytest

# import pytest

# def is_even(number):
#     return number % 2 == 0
#
# def test_even_number():
#     number = 4
#     assert is_even(number) == True
#
# def test_odd_number():
#     number = 7
#     assert is_even(number) == False


#3 Pytest

import pytest

# def len_num(number):
#     return len(str(number))
#
# def test_len_number():
#     number = 9299
#     assert len_num(number) == 4

#4 pytest

# import pytest
#
# def sum_of_list(list):
#     return sum(list)
#
# def test_sum_of_list():
#     list = [1, 2, 3, 4, 5]
#     assert sum_of_list(list) == 15

#5 Pytest

# import pytest
#
# def sum_of_numbers(list_str):
#     numbers = [int(x) for x in list_str.split(",")]
#     return sum(numbers)
#
# def test_sum_of_numbers():
#     list_str = '12,34,56'
#     assert sum_of_numbers(list_str) == 102


#1 Unittest

# import unittest
#
# def convert_date_to_tuple(date_string):
#     year, month, day = date_string.split('-')
#     return (day, month, year)
#
# class TestDateConversion(unittest.TestCase):
#     def test_convert_date_to_tuple(self):
#         date_string = '2025-12-31'
#         self.assertEqual(convert_date_to_tuple(date_string), ('31', '12', '2025'))
#
# if __name__ == '__main__':
#     unittest.main()

#2 Unittest

# import unittest
#
# def sum_of_list_elements(lst):
#     return sum(int(x) for x in lst)
#
# class TestSumOfListElements(unittest.TestCase):
#     def test_sum_of_list_elements(self):
#         self.assertEqual(sum_of_list_elements(['1', '2', '3', '4', '5']), 15)
#
# if __name__ == '__main__':
#     unittest.main()

#3 Unittest

# def divide_sum_of_halves(lst):
#     middle = len(lst) // 2
#     first_half_sum = sum(lst[:middle])
#     second_half_sum = sum(lst[middle:])
#     return first_half_sum / second_half_sum
#
#
# import unittest
#
# class TestDivideSumOfHalves(unittest.TestCase):
#     def test_divide_sum_of_halves(self):
#         self.assertEqual(divide_sum_of_halves([1, 2, 3, 4, 5, 6]), 0.4375)
#
# if __name__ == '__main__':
#     unittest.main()

#4 Unittest
# def merge_dicts(dct1, dct2):
#     return {**dct1, **dct2}
#
#
# import unittest
#
# class TestMergeDicts(unittest.TestCase):
#     def test_merge_dicts(self):
#         dct1 = {'a': 1, 'b': 2}
#         dct2 = {'c': 3, 'd': 4}
#         self.assertEqual(merge_dicts(dct1, dct2), {'a': 1, 'b': 2, 'c': 3, 'd': 4})
#
# if __name__ == '__main__':
#     unittest.main()

#5 Unittest

import unittest

# def sum_of_values(dct):
#     total_sum = 0
#     for inner_dict in dct.values():
#         for value in inner_dict.values():
#             total_sum += value
#     return total_sum
#
# class TestSumOfValues(unittest.TestCase):
#
#     def test_sum_of_values(self):
#         dct = {
#             1: {1: 11, 2: 12, 3: 13},
#             2: {1: 21, 2: 22, 3: 23},
#             3: {1: 24, 2: 25, 3: 26}
#         }
#         self.assertEqual(sum_of_values(dct), 207)
#
# if __name__ == '__main__':
#     unittest.main()

#5

# def max_min_values(numbers):
#     if len(numbers) == 0:
#         return None
#     max_val = max(numbers)
#     min_val = min(numbers)
#     return {'max': max_val, 'min': min_val}
#
#
# numbers = [1, 5, 9, 3, 7]
# result = max_min_values(numbers)
# print(result)

#6

# def find_divisors(numbers):
#     result = []
#     for num in numbers:
#         divisors = [i for i in range(1, num+1) if num % i == 0]
#         result.append(divisors)
#     return result
#
#
# numbers = [6, 8, 12]
# result = find_divisors(numbers)
# print(result)

#7

# import random
#
# def generate_unique_numbers(N, start, end):
#     result = []
#     while len(result) < N:
#         num = random.randint(start, end)
#         if num not in result or len(result) == 0:
#             result.append(num)
#     return result
#
#
# unique_numbers = generate_unique_numbers(5, 1, 10)
# print(unique_numbers)

#8

# import random
#
# def get_random_color():
#     colors = ['red', 'blue', 'green', 'yellow', 'purple']
#     return random.choice(colors)
#
#
# color = get_random_color()
# print(color)

#9

# def syllables(word):
#     glas = "aeiouy"
#     syllable_list = []
#     current_syllable = ""
#
#     for letter in word:
#         if letter in glas:
#             current_syllable += letter
#             syllable_list.append(current_syllable)
#             current_syllable = ""
#         else:
#             current_syllable += letter
#
#     if current_syllable:
#         syllable_list.append(current_syllable)
#
#     return syllable_list
#
#
#
# word = "alabuga"
# result = syllables(word)
# print(result)

#10
# import random
#
# def shuffle_list(input_list):
#     random.shuffle(input_list)
#     return input_list
#
#
# my_list = [1, 2, 3, 4, 5]
# result = shuffle_list(my_list)
# print(result)

