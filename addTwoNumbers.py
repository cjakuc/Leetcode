# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        bool_temp = True
        while bool_temp:
            num1 = str(l1.val) + num1
            if l1.next == None:
                break
            l1 = l1.next
        while bool_temp:
            num2 = str(l2.val) + num2
            if l2.next == None:
                break
            l2 = l2.next


        num3 = str(int(num1) + int(num2))
        num3 = num3[::-1]
        
        first_node = ListNode(val=int(num3[0]))
        current_node = first_node
        for num in num3[1:]:
            current_node.next = ListNode(val=int(num))
            current_node = current_node.next
        
        return first_node
