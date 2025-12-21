def count_nums(nums):
    hm = {}

    for num in nums:
        if num in hm:
            hm[num] += 1
        else:
            hm[num] = 1
    
    return hm

nums = [2,3,2,4,5,3,2]
print(count_nums(nums))