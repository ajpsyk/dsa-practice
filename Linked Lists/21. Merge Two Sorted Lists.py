# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = ListNode(None)
        current = merged_list

        while list1 and list2:
            if list2.val < list1.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next
        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
        
        return merged_list.next