def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for idx1 in range(len(nums)):
        remain = target - nums[idx1]
        if remain not in nums[idx1+1::]:
            continue
        elif remain in nums[idx1+1::]:
            idx2 = nums.index(remain)
            if idx2 == idx1:
                nums[idx1] = "_"
            idx2 = nums.index(remain)
            return [idx1, idx2]