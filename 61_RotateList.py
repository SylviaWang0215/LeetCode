class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rorateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if k == 0:
            return head

        count = 1
        old_head = head
        temp = head
        while temp.next:
            temp = temp.next
            count += 1
        step = count - k % count
        if step == count:
            return head
        new_head = head
        new_tail = None
        for i in range(step):
            new_tail = new_head
            new_head = new_head.next

        new_tail.next = None

        tail = new_head
        if tail == None:
            tail.next = old_head
        else:
            while tail.next:
                tail = tail.next
        tail.next = old_head
        return new_head
