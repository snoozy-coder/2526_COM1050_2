from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                                    #Nếu danh sách rỗng
            return 0                                    #Trả ra 0
        
        l = 0                                           #Tạo con trỏ trái

        for r in range(1,len(nums)):                    #Do mảng đã được sắp xếp, duyệt con trỏ phải từ 1 đến hết
            if nums[l] != nums[r]:                      #Nếu số tại trỏ trái khác số tại trỏ phải
                l += 1                                  #Tăng trỏ trái lên
                nums[l] = nums[r]                       #Gắn số tại trỏ trái bằng số tại trỏ phải
                
        return l + 1                                    #Trả ra kết quả bằng vị trị của trỏ trái + 1
    #Time: O(n) - Duyệt từ vị trí 1 đến hết mảng
    #Space: O(1) - Không tạo thêm mảng phụ


        