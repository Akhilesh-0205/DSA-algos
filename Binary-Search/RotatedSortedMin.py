from Array_definition import print_array, Rotated_array
nums = Rotated_array

#this question can be done in two ways using binary search.
#method one (easier to understand)
def findMin1(nums):
    minimum = float('inf')
    s = 0
    e = len(nums) - 1
    while s <= e:
        mid = (s + e) // 2
        if nums[mid] >= nums[s]:    #means left part is sorted, so we just take the first el of left half.
            minimum = min(minimum, nums[s])
            s = mid + 1
        else: #if left part is not sorted means mid could also be the answer cauz its also the first el of sorted right part.
            minimum = min(minimum, nums[mid])
            e = mid - 1
    return minimum

if __name__ == "__main__":
    print("Array:")
    print_array(nums)
    print("minimum in array is:")
    ans = findMin1(nums)
    print(ans)