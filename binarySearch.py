numberList = [1,2,3,4,6,7,8,10,11,12]

# find the value middle index
# compare to target
# if target is less, di
def binarySearch(target, nums):
    high = len(nums) - 1
    low = 0
    while high >= low :
        mid = (high + low)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binarySearch(13, numberList))