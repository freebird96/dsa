# Given a list of elements find all combination of the list using the elements in hte list.
# For Eg: [1,2,3] ==> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def decimalToBinary(n):
    return "{0:b}".format(int(n))
    


# Time complexity: O(2^N*N).
def get_subsets(num_list):
    final_set = []
    for i in range(1<<len(num_list)):
        current_set = []
        for j in range(len(num_list)):
            if (i & 1<<j)>0:
                print(i, j, decimalToBinary(i) , decimalToBinary(1<<j))
                current_set.append(num_list[j])
        final_set.append(current_set)
    return final_set

if __name__ == '__main__':
    num_list = [1,2,3]
    res = get_subsets(num_list)
    print(res)

