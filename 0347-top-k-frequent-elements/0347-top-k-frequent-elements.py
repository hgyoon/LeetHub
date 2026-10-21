class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        temp_d = {}
        for num in nums:
            temp_d[num] = temp_d.get(num, 0) + 1
        return sorted(temp_d, key=temp_d.get, reverse=True)[:k]