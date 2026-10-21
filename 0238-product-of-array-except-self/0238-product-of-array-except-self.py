class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # N개의 1들 만들기 (1로 해야 곱하기 가능)
        output = [1] * len(nums)
        # temp base 숫자 하나 만들기 (for memory)
        left = right = 1
        # 자신의 왼쪽을 다 곱하기 - 순서 중요
        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            output[j] *= right
            right *= nums[j]
        return output