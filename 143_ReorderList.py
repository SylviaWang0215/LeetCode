# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #first count the length of the linked list
        temp = head
        if head is None:
            return head
        count = 1
        stack = []
        queue = []

        while temp.next is not None:
            stack.append(temp.val)
            temp = temp.next
            count += 1
        print count

        for i in range(count / 2):
            old_next = head.next
            head.next.val = stack.pop()
            head.next.next = old_next
            head = old_next


lis = [1, 2, 3, 4]
f = Solution()
f.reorderList(lis)
print lis

