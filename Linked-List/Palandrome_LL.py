from LL_definition import LinkedList, printLL

def reverseLL(head): #we have already written reverse logic in previous file.
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def isPalandrome(head):
    #the approach is that we reverse one half of the list and check if both halfs are same.
    #checking edge case.
    if head == None or head.next == None:
        return True
    #first step is to find mid.
    slow = head #see how both slow and fast are on head first to find mid.
    fast = head
    while fast != None and fast.next!= None:
        fast = fast.next.next
        slow = slow.next
    #now that we have got our mid slow, we will reverse the next half from mid.
    second_head = reverseLL(slow.next)
    #now that we have both the halfs we will compare it.
    first = head
    second = second_head
    while second != None:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True

if __name__ == "__main__":
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(2)
    node5 = LinkedList(1)
    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print("Oiginal List:")
    printLL(head)
    print("is the original List palandome:")
    if(isPalandrome(head)):
        print("yes")
    else:
        print("No")