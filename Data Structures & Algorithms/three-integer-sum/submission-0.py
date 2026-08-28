class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #two spaces for left and right
        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]: 
                continue
            
            cur = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                add = nums[left] + nums[right] 
                if add > cur:
                    right -= 1
                elif add < cur:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 避免內層數字重複產生相同組合
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans
            


            
            
