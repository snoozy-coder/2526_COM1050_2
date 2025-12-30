from typing import List 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:  
        i = len(s) - 1                          #Tạo biến i để duyệt xâu từ cuối xuống
        cnt = 0                                 #Tạo biến đếm
        
        while i >= 0 and not s[i].isalpha():    #Loại bỏ các kí tự không phải chữ cái
            i -= 1

        while i >= 0 and s[i].isalpha():        #Đếm các kí tự trong từ cuối cùng
            cnt +=1                             
            i -= 1                              

        return cnt                              #Trả ra kết quả
    #Time: O(n)
    #Space: O(1)
        