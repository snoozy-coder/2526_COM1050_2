class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''                              #Biến lưu kết quả
        change = {                          #Hash map để chuyển giá trị nguyên thành kí tự La Mã
            1000: "M",
            900:  "CM",
            500:  "D",
            400:  "CD",
            100:  "C",
            90:   "XC",
            50:   "L",
            40:   "XL",
            10:   "X",
            9:    "IX",
            5:    "V",
            4:    "IV",
            1:    "I"
        }

        for key, value in change.items():   #Duyệt các cặp key và value từ lớn đến nhỏ
            s += value * (num // key)       #Lấy ra tối đa số lần xuất hiện của kí tự 
            num = num % key                 #Cập nhật lại số
            
        return s                            #Trả ra kết quả
    
    #Time: O(1) - Duyệt từ lớn đến nhỏ 13 cặp key và value cho mọi số nguyên
    #Space: O(1) - Luôn tạo hash map có 13 cặp key value cho mọi số nguyên
        