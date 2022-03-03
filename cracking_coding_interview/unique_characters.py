# implement an algorithm to determine if the given string only contains unique characters in it

import math
# Brute force
# Time complexity O(n^2), Space complexity: o(0)
# def unique_chars(word):
#     for i in range(len(word)):
#         for j in range(len(word)):
#             if i != j and word[i].lower() == word[j].lower():
#                 return True
#     return False

# # Time complexity : o(n) and space complexity: o(n)
# def unique_chars(word):
#     chars = {}
#     for i in word:
#         chars[i] = False
#     for i in word:
#         if not chars[i]:
#             chars[i] = True
#         else:
#             return True
#     return False

# Without using additional datastructures.
# Bit manupulation method
def unique_chars(word):
    checker = 0
    for i in word:
        print(checker)
        bit_index = ord(i)
        print(checker,bit_index,i,  checker & 1 << bit_index)
        if (checker & 1 << bit_index) > 0:
            return True
        checker = checker | 1 << bit_index
    return False




if __name__ == '__main__':
    word = input('Enter the word: ')
    print(unique_chars(str(word)))
    
