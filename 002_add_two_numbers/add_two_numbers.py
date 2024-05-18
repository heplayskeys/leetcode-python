class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
        
class Solution:
  def addTwoNumbers(self, l1, l2):
    head = ListNode()
    current = head
    carry = 0

    while l1 or l2 or carry:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0
      value = v1 + v2 + carry
      carry = value // 10
      current.next = ListNode(value % 10)

      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
      current = current.next
    
    return head.next
  

  def print_answer(self, l_node):
    output = []
    current = l_node

    while current:
      output.append(current.val)
      current = current.next
    print(output)


s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
s.print_answer(s.addTwoNumbers(l1, l2))

l3 = ListNode()
s.print_answer(s.addTwoNumbers(l3, l3))

l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
s.print_answer(s.addTwoNumbers(l4, l5))


### STRING CONVERSION METHOD
        
# class Solution:
#   def addTwoNumbers(self, l1, l2):
#     v1 = [l1.val]
#     v2 = [l2.val]

#     current = l1.next
#     while current:
#       v1 = [current.val, *v1]
#       current = current.next
    
#     current = l2.next
#     while current:
#       v2 = [current.val, *v2]
#       current = current.next

#     v1 = [str(num) for num in v1]
#     v2 = [str(num) for num in v2]
#     sum = int("".join(v1)) + int("".join(v2))
#     sum_str = [*str(sum)]

#     return [int(num) for num in sum_str][::-1]