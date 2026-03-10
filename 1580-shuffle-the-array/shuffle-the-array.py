class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):

            x_value = nums[i]

            y_value = nums[i+n]

            result.append(x_value)
            result.append(y_value)
        return result