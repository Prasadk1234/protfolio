# Add two numbers with simple one
arr = [2,7,11,15]
target = 18
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] == target - arr[i]:
            print(i , j)

# Add two numbers with linklist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]):
        head = ListNode(0)
        root = head
        carry = 0

        while l1 or l2:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0
            s = v1 + v2 + carry

            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry :
            head.next = ListNode(carry)

        return root.next


lr = Solution()
lr.addTwoNumbers(l1=[2,4,3],l2=[5,6,4])



