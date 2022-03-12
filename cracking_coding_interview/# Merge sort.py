# Merge sort


def merge_sort(array):
    # 1. Divide the arrray into two parts
    # 2. Sort each parts independently 
    # 3. Add the remaining ones onto that array and merge it together.
    # 4. Combine the two halves.
    if len(array) == 1:
        return array
    mid = len(array) // 2
    L = array[:mid]
    R = array[mid:]
    merge_sort(R)
    merge_sort(L)
    i = j = k = 0
    while i < len(L) and j<len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        array[k] = L[i]
        k += 1
        i += 1
    
    while j < len(R):
        array[k] = R[j]
        k += 1
        j += 1
    
    return array

print(merge_sort([9,8,7,6,5,4,3,2,1,0]))





