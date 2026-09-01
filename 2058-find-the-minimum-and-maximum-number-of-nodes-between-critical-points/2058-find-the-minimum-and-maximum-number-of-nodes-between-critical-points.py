# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]
        #we have to keep track of first critical point and keep finding last critical point and checking distance between last found critical point and last critical point to find minimum.
        #At the end maximum distance will just be last - first criticacl point.
        first = -1
        last = -1
        prev = head
        curr = prev.next
        nex = curr.next
        pos = 1
        dis = 0
        minima = float('inf')
        while curr.next != None:
            if (curr.val > prev.val and curr.val > nex.val) or (curr.val < prev.val and curr.val < nex.val):
                if first == -1:
                    first = pos
                else:
                    dis = pos - last
                    if dis < minima:
                        minima = dis
                last = pos
            prev = curr
            curr = nex
            nex = nex.next
            pos += 1
        if first == -1 or first == last:
            return [-1, -1]
        maxima = last - first
        return[minima, maxima]
