from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}                           #Tạo hash map

        for s in strs:                          #Duyệt các từ
            key = ''.join(sorted(s))            #Lấy key là từ đó sau khi sắp xếp
            if key not in hash_map:             #Nếu chưa có
                hash_map[key] = [s]             #Thêm vào hash map
            else:                               #Nếu đã có trong hash map
                hash_map[key].append(s)         #Thêm vào danh sách các từ có cùng key

        return list(hash_map.values())          #Trả ra kết quả là danh sách gồm các danh sách con các từ cùng nhóm
#Time: O(N)
#Space: O(N)