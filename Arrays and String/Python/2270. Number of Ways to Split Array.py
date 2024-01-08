class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # build a prefix sum
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        # answer to keep track of how many valid way to split the array
        ans = 0
        # loop through prefix sum, compare the left sum (current at i) and the right sum (from i+1 to end <=> prefix[-1] - prefix[i]) 
        # loop until i-1 since we cannot split at the last index
        for i in range(len(prefix) - 1):
            left_sum = prefix[i]
            right_sum = prefix[-1] - prefix[i]
            if left_sum >= right_sum:
                ans += 1

        return ans
