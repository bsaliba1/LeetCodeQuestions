 #Definition for singly-linked list.

 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        print(head.val)

def createList(arr = [1,2,3,4,5]) -> ListNode:
    head = ListNode(arr[0])
    temp = head
    for i in range(1,arr.len()):
        temp.next = ListNode(arr[i])
        temp = temp.next

createList([1,2,3,4,5])
