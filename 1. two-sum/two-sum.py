class Solution:
  def two_sum_On2(self, nums, target):
    # Brute force O(n^2) with nested for loop to check all possible number combinations.
    for idx1 in range(len(nums)):
      for idx2 in range((idx1 + 1), len(nums)):
        if target == (nums[idx1] + nums[idx2]):
          return [idx1, idx2]

  def two_sum_On(self, nums, target):
    # Achieve O(n) by using hashmap with key:value pairs in number:index form.
    hash = {}
    for i in range(len(nums)):
      hash[nums[i]] = i
    for i in range(len(nums)):
      comp = target - nums[i]
      if comp in hash and hash[comp] != i:
        return [i, hash[comp]]


s = Solution()
print(s.two_sum_On2(nums=[2,7,11,15], target=9)) # [0, 1]
print(s.two_sum_On(nums=[2,7,11,15], target=9)) # [0, 1]

print(s.two_sum_On2(nums=[3,2,4], target=6)) # [1, 2]
print(s.two_sum_On(nums=[3,2,4], target=6)) # [1, 2]

print(s.two_sum_On2(nums=[3,3], target=6)) # [0, 1]
print(s.two_sum_On(nums=[3,3], target=6)) # [0, 1]
