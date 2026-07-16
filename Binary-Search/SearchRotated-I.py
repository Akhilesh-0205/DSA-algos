from Array_definition import Rotated_array, print_array
#Approach is that we check which half is sorted and than check if target lies in the sorted half.

def SearchInRotatedArray(Rotated_array, target):
    s = 0
    e = len(Rotated_array) - 1
    while s <= e:
        mid = (s + e) // 2
        if Rotated_array[mid] == target:
            return mid
        elif Rotated_array[mid] >= Rotated_array[s]: #left is sorted
            if Rotated_array[s] <= target < Rotated_array[mid]: #target lies in sorted half
                e = mid - 1
            else: #target lies in unSorted half
                s = mid + 1
        else:
            if Rotated_array[mid] < target <= Rotated_array[e]:
                s = mid + 1
            else:
                e = mid - 1
    return None

if __name__ == "__main__":
    print("Array:")
    print_array(Rotated_array)
    print("target lies on index:")
    ans = SearchInRotatedArray(Rotated_array, 1)
    print(ans)