from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1               #Tạo hai con trỏ ở đầu và cuối danh sách
        mx = 0                                  #Tạo biến để lưu diện tích

        while l < r:                            #Tạo vòng lặp
            mx = max(mx, min(height[l],height[r]) * (r-l))  #Cập nhập diện tích lớn nhất

            if height[l] < height[r]:           #Nếu cột trái đang thấp hơn cột phải
                l +=1                           #Dịch cột trái
            else:                               #Ngược lại
                r -=1                           #Dịch cột phải

        return mx                               #Trả ra diện tích 
    
    #Time: O(n) - Duyệt tối đa n
    #Space: O(1) - Không tạo thêm mảng phụ