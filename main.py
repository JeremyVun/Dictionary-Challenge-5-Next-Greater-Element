"""
Dictionary Challenge 5 - Next Greater Element

Description:
You are given two distinct arrays of integers nums1 and nums2. nums1 is a subset of numse2 i.e. all the numbers of nums1 are also in nums2.

Each integer x in nums1 appears in nums2. Your job is to find the first integer to the right of x in nums2 that is greater than x.

Example:
Input:
  nums1 = [4, 1, 3]
  nums2 = [3, 1, 4, 2]
Correct Output:
  [-1, 4, 4]
Explanation:
  -1: 4 appears at nums2[2] There is no number greater than it to the right (only the number 2), therefore return -1
  4: 1 appears at nums2[1]. The next highest number in nums2 is 4 at nums2[2].
  4: 3 appears at nums2[0]. The next highest number in nums2 is 4 at nums2[2]
"""

from solution import fast


########
# Write your code in this function
########
def solution(nums1, nums2):
  return fast(nums1, nums2)



########
# This code wil run your solution against a bunch of test cases
########
from tests.runner import run

if __name__ == "__main__":
  run(solution)