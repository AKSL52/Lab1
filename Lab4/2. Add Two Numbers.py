from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def create_linked_list(arr: list) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == '__main__':
    solution = Solution()

    l1_1 = create_linked_list([2, 4, 3])
    l2_1 = create_linked_list([5, 6, 4])
    result_1 = solution.addTwoNumbers(l1_1, l2_1)
    print(f"Example 1: {linked_list_to_list(result_1)}")

    l1_2 = create_linked_list([0])
    l2_2 = create_linked_list([0])
    result_2 = solution.addTwoNumbers(l1_2, l2_2)
    print(f"Example 2: {linked_list_to_list(result_2)}")

    l1_3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2_3 = create_linked_list([9, 9, 9, 9])
    result_3 = solution.addTwoNumbers(l1_3, l2_3)
    print(f"Example 3: {linked_list_to_list(result_3)}")