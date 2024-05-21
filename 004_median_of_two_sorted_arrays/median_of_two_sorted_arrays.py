class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    """
    nums1: List[int]
    nums2: List[int]
    return: (List[int]) -> float
    """
    m, n = len(nums1), len(nums2)
    result = [0] * (m + n) # OR # result = [] for append method
    i = 0
    j = 0

    while (i + j) < (m + n):
      if i < m and j < n:
        if nums1[i] < nums2[j]:
          result[i + j] = nums1[i] # OR result.append(nums1[i])
          i += 1
        else:
          result[i + j] = nums2[j] # OR result.append(nums2[j])
          j += 1
      elif i < m:
        result[i + j] = nums1[i] # OR result.append(nums1[i])
        i += 1
      else:
        result[i + j] = nums2[j] # OR result.append(nums2[j])
        j += 1
        
    return self.calc_median(result)
  
  def calc_median(self, nums):
    """
    nums: List[int]
    return: float
    """
    if len(nums) % 2 != 0:
      return nums[len(nums) // 2] / 1
    
    num1 = nums[(len(nums) // 2) - 1]
    num2 = nums[len(nums) // 2]
    return (num1 + num2) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([1, 2, 10], [4, 6, 16, 17]))
