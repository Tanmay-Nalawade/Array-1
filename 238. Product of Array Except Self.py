# Time Complexity : O(n)
# Space Complexity : O(n) leaving the output array
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english
    # - Form the result array with everything as 1
    # - Do the left pass with running product
    # - Then do the right pass muliplying with the current left pass elements of the array

# Your code here along with comments explaining your approach

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result= [1] * n

        product = 1
        for i in range(n):
            result[i] = product
            product = product * nums[i]

        product = 1
        for i in range(n-1,-1,-1):
            result[i] = product * result[i]
            product *= nums[i]

        return result