class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = j = 0                                           #Tạo 2 con trỏ

        while i < len(haystack) and j < len(needle):        #So sánh kí tự tại hai con trỏ
            if haystack[i] == needle[j]:                    #Nếu hai kí tự giống nhau
                i += 1                                      #Tăng trỏ i
                j += 1                                      #Tăng trỏ j
            else:                                           #Nếu hai kí tự khác nhau
                i = i - j + 1                               #Đưa con trỏ i lùi lại j+1 bước                               
                j = 0                                       #Đưa con trỏ j về lại kí tự đầu tiên 

        if j == len(needle):                                #Nếu xâu needle được duyệt hết  
            return i - j                                    #Trả ra index của needle[0] trong haystack
        else:                                               #Nếu không được duyệt hết
            return -1                                       #Trả ra -1
#Time: O(N)
#Space: O(1)

        