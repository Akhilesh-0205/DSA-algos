from LL_definition import LinkedList, printLL
#we have to detect if there is a loop in the linked list.
#we will use floyd's tortoise and hare algo.
#if there is a loop fast will 100% catchup with the slow and ultimatly both will be at the same node.
def isLoop(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 #loop
    
    head = node1

    #we cannot print cauze of loop
    print("Does the input LL has Loop:")
    ans = isLoop(head)
    print(ans)