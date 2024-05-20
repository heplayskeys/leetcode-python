class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    longest_substr = 0
    substr = set()

    for ltr in s:
      if ltr in substr:
        if len(substr) > longest_substr:
          longest_substr = len(substr)
        substr = set()
      substr.add(ltr)
    
    return longest_substr
  
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
