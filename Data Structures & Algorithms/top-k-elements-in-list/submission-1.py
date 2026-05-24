class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        if len(nums) < 1:
            return []
    

        sorted_nums = sorted(nums)

        for val in sorted_nums:
            if val in mapping:
                mapping[val] += 1
            else: 
                mapping[val] = 1
        
        res = sorted(mapping.keys(), key=lambda x: mapping[x], reverse=True)
        return res[:k]