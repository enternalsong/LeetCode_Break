class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right, left = 0, len(nums) - 1
        while right < left:
            mid = (right + left) // 2
            if nums[mid] < target:
                right = mid + 1
            else:
                left = mid
        return left if nums[left] == target else -1