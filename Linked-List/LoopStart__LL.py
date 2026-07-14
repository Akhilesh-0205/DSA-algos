from LL_definition import LinkedList, printLL

def findStartingPoint(head):
    #the approach to detect the loop is simple but to find the starting point is a little mathematical.
    #first step to detect the loop.
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        #if they collide loop detected
        if slow == fast:
            #now to find starting point-> the intuition,
            #when they have collided there is exactly L distance to the starting point
            #which is equal to (head to start) and (collide to start).
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

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

    print("starting point of the LL:")
    start = findStartingPoint(head)
    print(start.val)