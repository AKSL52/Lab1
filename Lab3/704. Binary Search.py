class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))