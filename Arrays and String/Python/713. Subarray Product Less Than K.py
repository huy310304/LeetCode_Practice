class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
    
        left = answer = 0
        curr = 1 # keep track of the product

        # open the windows to the right
        for right in range(len(nums)):
            curr *= nums[right]

            # if the product pass the limit (curr >= k)
            while curr >= k: 
                # shrink the window, update the product
                curr //= nums[left] 
                left += 1
            
            # count the numbers of the subarray ending with right
            # the number of valid windows ending at index right is equal to the size of the window, 
            # which we know is right - left + 1
            answer += (right - left + 1)

        # return the answer
        return answer
