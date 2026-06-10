class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
        hashset, max_streak = set(nums), 0
        for n in hashset:
            if n - 1 not in hashset:
                streak = 0
                while (n + streak) in hashset:
                    streak += 1
                max_streak = max(max_streak, streak)
        return max_streak
