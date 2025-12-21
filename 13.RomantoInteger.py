class Solution:
    def romanToInt(self, s: str) -> int:
        values = {                          #Tạo hash map chuyển từ kí tự ra giá trị nguyên                       
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
        total = 0                           #Biến lưu kết quả
    
        for i in range(len(s)):             #Duyệt các kí tự của s
            
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:    #Nếu kí tự sau không vượt quá idx và giá trị tương ứng lớn hơn kí tự hiện tại
                total -= values[s[i]]       #Trừ đi giá trị nguyên của kí tự hiện tại                     
            else:                           
                total += values[s[i]]       #Cộng thêm giá trị nguyên của kí tự hiện tại

        return total                        #Trả ra kết quả
    #Time: O(n) - Duyệt tất cả các chữ số của xâu
    #Space: O(1) - Hash map chung cho tất cả các xâu
