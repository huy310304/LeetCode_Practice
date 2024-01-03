class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            left = 0
            curr = 0 # keep track of zeros
            ans = 0 # keep track of the longest length
            
            # expanding the windows to the right
            for right in range(len(nums)):
                
                if nums[right] == 0:
                    curr += 1
                
                while curr > k:
                    if nums[left] == 0:
                        curr -= 1
                    left += 1

                ans = max(ans, right-left+1)

            return ans
        
