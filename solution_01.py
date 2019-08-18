#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
# -*- conding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #用n表示nums的长度
        n = len(nums)
        #x取值从0取到n（不包括n）
        for x in range(n):
            #y取值从x+1取值到n（不包括n）
            for y in range(x+1, n):
                #如果target - nums[x]存在与nums中
                if nums[y] == target - nums[x]:
                    return x, y
                    break
                else:
                    continue
    def twoSum_1(sef, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        利用字典来解决，效率更高
        """
        #用l表示nums的长度
        l = len(nums)
        #创建一个空字典
        d = {}
        for x in range(l):
            a = target - nums[x]
            #字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]], x
            #否则往字典里增加键值对
            else:
                d[a] = x
        #边往字典里增加键值对，边与nums[x]进行比较

s = Solution()
print(s.twoSum([1,2,3,4,5],9))
print(s.twoSum_1([1,2,3], 3))

