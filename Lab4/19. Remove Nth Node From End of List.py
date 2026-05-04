from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

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

    head1 = create_linked_list([1, 2, 3, 4, 5])
    res1 = solution.removeNthFromEnd(head1, 2)
    print(f"Example 1: Input: [1, 2, 3, 4, 5], n=2 -> Output: {linked_list_to_list(res1)}")

    head2 = create_linked_list([1])
    res2 = solution.removeNthFromEnd(head2, 1)
    print(f"Example 2: Input: [1], n=1 -> Output: {linked_list_to_list(res2)}")

    head3 = create_linked_list([1, 2])
    res3 = solution.removeNthFromEnd(head3, 1)
    print(f"Example 3: Input: [1, 2], n=1 -> Output: {linked_list_to_list(res3)}")