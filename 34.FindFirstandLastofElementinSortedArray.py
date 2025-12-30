from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        l, r = 0, n

        while l <= r:
            mid = (l+r)//2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        if r < 0 or nums[r] != target:
            return [-1,-1]
        else:
            i = r

        l, r = 0, i - 1

        while l <= r:
            mid =(l+r)//2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [r+1, i]

