from Array_definition import print_array, Duplicate_Rotated_array
#we have to return Ture if target exists in duplicate rotated array.

nums = Duplicate_Rotated_array

def SearchInRotated(nums, target):
    s = 0
    e = len(nums) - 1
    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[s] == nums[e]: #Case to handle duplicates.
            s += 1
            e -= 1
            continue
        elif nums[mid] >= nums[s]: #left is sorted
            if nums[s] <= target < nums[mid]: #target lies in sorted half
                e = mid - 1
            else: #target lies in unSorted half
                s = mid + 1
        else:
            if nums[mid] < target <= nums[e]:
                s = mid + 1
            else:
                e = mid - 1
    return False

if __name__ == "__main__":
    print("Array:")
    print_array(nums)
    print("Does target lies?:")
    ans = SearchInRotated(nums, 1)
    print(ans)