from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


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

    input_1 = [1, 2, 3, 4, 5]
    head_1 = create_linked_list(input_1)
    result_1 = solution.reverseList(head_1)
    print(f"Example 1: Input: {input_1} -> Output: {linked_list_to_list(result_1)}")

    input_2 = [1, 2]
    head_2 = create_linked_list(input_2)
    result_2 = solution.reverseList(head_2)
    print(f"Example 2: Input: {input_2} -> Output: {linked_list_to_list(result_2)}")
