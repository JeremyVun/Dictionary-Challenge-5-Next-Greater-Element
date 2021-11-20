def fast(nums1, nums2):
  greater = {}
  stack = []

  # Iterate once through nums2 and registry all the next greater numbers into a dictionary
  for n2 in nums2:
    while stack and n2 > stack[-1]:
      prev_num = stack.pop(-1)
      greater[prev_num] = n2
    stack.append(n2)

  # Iterate once through nums1 to finalise all the answers by looking up our dictionary!
  result = []
  for n1 in nums1:
    if n1 in greater:
      greater_num = greater[n1]
      result.append(greater_num)
    else:
      result.append(-1)

  return result