"""
  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.  
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    
"""
# Time complexity : O(n)
# Space complexity: O(1) - only the two items are being stored in the execution.
def kadanesAlgorithm(array):
    # Write your code here.
    current_max = 0
    max_so_far = array[0]
    for num in array:
        current_max = max(current_max+num, num)
        max_so_far = max(current_max, max_so_far)

    return max_so_far





