from typing import List
from functools import reduce


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Ret vals
        retArr = []
        max = 0

        #Counting vals
        split = 2
        while(split <= len(nums)):
            current = 0
            for i in range(int(len(nums)/split)):
                sum = reduce(lambda a,b: a+b, nums[current:current+split])
                if sum > max:
                    max = sum
                    retArr = nums[current:split]
                current = current+split
            split = split*2
        return retArr


def maxSubArraySum(a):
    retArr = []
    max_so_far = -float("inf") #start max so far as negative inf
    max_ending_here = 0
    begin = 0
    end = 0

    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = i
        else:
            begin = i

        if max_ending_here < 0:
            max_ending_here = 0

    print("begin:", begin)
    print("end:", end)

    if end < begin:
        return a[0:end+1]
    else:
        return a[begin+1:end+1]

# Driver function to check the above function
a = [1,2,15,-18,8,4]
print("Maximum contiguous sum is", maxSubArraySum(a))


#sol = Solution()
#print(sol.maxSubArray([1,2,3,4]))


