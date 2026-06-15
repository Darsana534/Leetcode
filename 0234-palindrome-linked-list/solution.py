# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        ptr=head
        while ptr!=None:
            vals.append(ptr.val)
            ptr=ptr.next
        if vals==vals[::-1]:
            return True
        else:
            return False
           
        
