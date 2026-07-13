from LL_definition import LinkedList, printLL

# If they intersect, they will eventually collide at the exact intersection node. Why? Because ptrA traverses Length(A) + Length(B), and ptrB traverses Length(B) + Length(A). They travel the exact same total distance, forcing them to sync up at the intersection!If they do not intersect, they will both hit the end of their second list (None) at the exact same time.

def intersaction(headA, headB):
    if headA == None or headB == None:
        return None
    ptrA = headA
    ptrB = headB
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    return ptrA

if __name__ == "__main__":
    node1 = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4 = LinkedList(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    headA = node1         #LL1

    node5 = LinkedList(5)
    node5.next = node3
    headB = node5         #LL2

    print("origina LLs:")
    printLL(headA)
    print("second one:")
    printLL(headB)

    intersact = intersaction(headA, headB)
    print("intersaction Node:")
    print(intersact.val)