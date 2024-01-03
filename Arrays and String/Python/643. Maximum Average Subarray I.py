class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0

        # build a fixed size(k) window 
        for i in range(k):
            curr += nums[i]

        # find the avg value by dividing the size of the subarray, which is k
        avg = curr / k
        
        # ans is used to find the maximum avg value 
        ans = avg

        # move the window to the right, same size(k)
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k] # update curr sum
            avg = curr / k # update avg value
            ans = max(ans, avg) # update max avg value

        return ans
