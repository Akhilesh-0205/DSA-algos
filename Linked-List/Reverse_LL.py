from LL_definition import LinkedList, printLL

#The logic to reverse a LL is just that we have to reverse the arrows.
#Firstly we need two pointers for the two nodes that we want to reverse.
def reverseLL(head):
    if head == None or head.next == None: #edge case
        return head
    prev = None
    curr = head
    while curr != None:
        temp = curr.next #we are making temp just so we dont lose connection with curr.next node.
        curr.next = prev
        prev = curr
        curr = temp
    return prev

if __name__ == "__main__":
    #Initialize the linked list
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    head = node1

    #Print original list
    print("Original List:")
    printLL(head)

    #Reverse List
    new_head = reverseLL(head)

    #Print reversed list
    print("\nReversed List:")
    printLL(new_head)
