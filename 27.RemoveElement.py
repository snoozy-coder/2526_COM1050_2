from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0                                                   #Đặt trỏ trái bằng 0

        for r in range(len(nums)):                              #Duyệt trỏ phải
            if nums[r] != val:                                  #Nếu số tại trỏ phải khác số cần lược bỏ
                nums[l] = nums[r]                               #Gán số đó vào số trái
                l += 1                                          #Tăng trỏ trái
        
        return l                                                #Trả ra kết quả
    #Time: O(n)
    #Space: O(1)
    
        