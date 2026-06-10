class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        res = []
        elem = 0 
        num_of_zero = 0
        # O(n)
        for elem in nums:
            if elem == 0: num_of_zero += 1
            total_product *= elem
        if num_of_zero > 1: return [0 for e in nums]
        if num_of_zero == 1:
            index = nums.index(0)
            res = [0 for i in nums]
            p = 1
            for i in range(len(nums)):
                if i == index: continue
                p *= nums[i]
            res[index] = p
            return res
        # num_of_zero == 0
        for elem in nums:
            res.append(total_product // elem)

        return res
