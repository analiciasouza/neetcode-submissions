class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size_nums = len(nums)
        map_nums = {}

        for i in range(size_nums):
            if nums[i] in map_nums:
                map_nums[nums[i]] += 1
            else:
                map_nums[nums[i]] = 1
        
        sorted_values = sorted(map_nums.items(), key=lambda p:p[1], reverse=True)
        result = []
        for i in range(len(sorted_values)):
            if len(result) < k:
               result.append(sorted_values[i][0])
        
        return result