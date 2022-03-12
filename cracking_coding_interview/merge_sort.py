# Given two strings check one is a permutation of the other
"""
# Questions to ask: 
    1. Check if permutation comparison is case sensitive
    2. Check if white spaces are to be considerered or trimmed.
    3. EG: Dog != God
"""
# [dog, god] returns True.
# [4,3,2,1,0,4,4,3, 2, 1]
# L=  [9,8,7,6,5] R = [4,3,2,1, 0] k=5
#     [9,8,7,6,5] [4,3,2,1, 0]
#     [4,8,7,6,5] [9,3,2,1, 0]


def merge_sort(array):
    """
        divide and conquer alorithm.
    """
    if len(array)==1:
        return array
    mid = len(array)//2
    L = array[:mid]
    R = array[mid:]
    # print(L, R)
    merge_sort(L)
    merge_sort(R)
    i=j=k=0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

    print( array)
    return array

merge_sort([9,8,7,6,5,4,3,2,1,0])
def check_permutation(string1, string2):
    """
        Returns a success message.
    """
    if len(string) != len(string):
        return False
    
    # for i in string

