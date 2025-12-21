class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:                                        #Nếu không phải xâu
            return ""                                       #Trả ra xâu rỗng

        rs = ""                                             #Biến lưu kết quả

        for i in range(len(strs[0])):                       #Duyệt các kí tự của phần tử đầu tiên
            spec = strs[0][i]                               #Đánh dấu kí tự đó

            for j in range(1,len(strs)):                    #Duyệt các kí tự còn lại                      
                if i >= len(strs[j]) or strs[j][i] != spec: #Nếu độ dài của xâu nhỏ hơn bằng i hoặc kí tự i của xâu j khác kí tự đánh dấu
                    return rs                               #Trả ra kết quả

            rs += spec                                      #Thêm kí tự được đánh dấu vào biến kết quả

        return rs                                           #Trả ra kết quả
    #Time: O(n x m) - Duyệt hết n phần tử trong danh sách và m kí tự của xâu ngắn nhất
    #Space: O(M) - Độ dài của biến kết quả là M với M là độ dài của prefix ngắn nhất
