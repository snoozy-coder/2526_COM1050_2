from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()                                    #Tạo set để kiểm tra kí tự trùng lặp
        l = 0                                           #Tạo con trỏ để kiểm tra kí tự ngoài cùng bên trái    
        mx = 0                                          #Tạo biến để lưu giá trị lớn nhất

        for r in range(len(s)):                         #Dùng con trỏ phải để duyệt chuỗi 
            while s[r] in seen:                         #Nếu gặp phần tử trùng lặp
                seen.remove(s[l])                       #Bỏ đi kí tự ngoài cùng bên trái
                l +=1                                   #Tăng con trỏ trái lên           
            
            seen.add(s[r])                              #Thêm kí tự hiện tại vào set          
            mx = max(mx, r-l+1)                         #Cập nhật độ dài lớn nhất

        return mx                                       #Trả ra độ dài lớn nhất
        
        #Time:O(n) - Duyệt hết chuỗi
        #Space:O(n) - Dùng set để lưu các kí tự đã sử dụng