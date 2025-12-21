class Solution:
    def isValid(self, s: str) -> bool:
        mp = []                         #Tạo stacks
        true = ["()","[]","{}"]         #Tạo list để kiếm tra 

        for i in s:                     #Duyệt các kí tự 
            if i in "([{":              #Nếu là ngoặc mở    
                mp.append(i)            #Thêm vào stacks
            elif not mp:                #Nếu không được thêm vào
                return False            #Trả ra False
            else:                       #Nếu là ngoặc mở
                t = mp.pop() + i        #Tạo biến để ghép ngoặc mở với ngoặc đóng được lấy ra từ stacks
                if t not in true:       #Nếu không trong danh sách đúng
                    return False        #Trả ra False
        
        return len(mp) == 0             #Trả ra kết quả bằng cách kiểm ra số phần tử còn lại trong stacks
    #Time: O(n) - Duyệt từng kí tự của xâu
    #Space: O(n) - Stacks để lưu các ngoặc mở