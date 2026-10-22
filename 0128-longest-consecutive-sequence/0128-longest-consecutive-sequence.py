class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # put everything in to a set
        nums_set = set(nums)
        output = 0
        for num in nums_set:
            # check if this is the start of sequence - nothing before it (no need to iterate until the beginnging)
            if num - 1 not in nums_set:
                count = 1
                # iterate until the endddd
                while num + 1 in nums_set:
                    count += 1
                    num += 1
                output = max(output, count)
        return output