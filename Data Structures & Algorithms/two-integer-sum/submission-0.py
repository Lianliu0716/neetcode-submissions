class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        half = target/2
        temp = {} 
        for i in range(0,len(nums)):
            if nums[i] in temp:
                return [temp[nums[i]], i]
            difference = target-nums[i]
            temp[difference] = i
        
            


