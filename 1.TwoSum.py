from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}                                               #Tạo hashmap để lưu các phần tử đã gặp

        for idx, num in enumerate(nums):                            #Duyệt idx và giá trị ứng với idx
            if target - num in hash_map:                            #Nếu hiệu của target và phần tử hiện tại đã có trong hashmap
                return [idx,hash_map[target - num]]                 #Trả ra idx của phần tử hiện tại và hiệu 
            hash_map[num] = idx                                     #Nếu chưa có, lưu trong hashmap với key là phần tử, value là idx của phần tử đó
                                                                    #Time: O(n) - Duyệt các phần tử trong mảng
                                                                    #Space: O(n) - Tạo hashmap để lưu các phần tử đã xuất hiện