class Solution(object):
    def uniformArray(self, nums1):
        #3 cases:
        #case1: all el are odd -> return True
        #case2: all el are even -> return True
        #case3: mix elements-> find smallest element, if smallest element in array is odd- return Ture, else return False,
        #Because if smallest is odd it will make all even odd by subtracting to them and it will 100% be >= 1 after subtraction.
        #if smallest is even than a smallest odd number will not have a smaller odd number to subtract to it to make it even.
        miniOdd = float('inf')
        for num in nums1:
            if num % 2 == 1:
                miniOdd = min(miniOdd, num)
        if miniOdd == float('inf'):
            return True #all elements are even
        for num in nums1:
            if num < miniOdd:
                return False #minimum element in array is even
        return True
        