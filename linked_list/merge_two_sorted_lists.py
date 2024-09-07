# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Iterative implemention
        head = ListNode()
        tail = head

        curr1, curr2 = list1, list2
        while curr1 or curr2:
            if curr1 and not curr2:
                tail.next = curr1
                break
            elif curr2 and not curr1:
                tail.next = curr2
                break
            else:
                if curr1.val <= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next
            tail = tail.next
        return head.next
    
        # Recursive implementation
        if (list1 == None): return list2
        if (list2 == None): return list1
        else:
            if (list1.val < list2.val):
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
            
        """
        NOTE: 
        solution:                     O(n) time, O(1) space
        """
