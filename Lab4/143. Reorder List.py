from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


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

    head1 = create_linked_list([1, 2, 3, 4])
    solution.reorderList(head1)
    print(f"Example 1: {linked_list_to_list(head1)}")

    head2 = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head2)
    print(f"Example 2: {linked_list_to_list(head2)}")