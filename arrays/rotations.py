def get_num_rotations(nums):

    if not nums: return -1
    lo =0
    hi = len(nums)-1
    while (lo <= hi):
        mid = (lo + hi)//2
        if (mid < hi and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]) or \
            (mid == hi and nums[mid] < nums[mid-1]):
            return mid
        elif nums[mid] >= nums[hi]:
            lo=mid + 1
        else:
             hi = mid - 1

    return 0

def get_pos_rotated_array(nums, elem):

    if not nums: return -1

    lo = 0
    hi = len(nums) -1

    while lo <= hi:
        
        mid = (lo + hi) //2
        print(f" Hi : {hi} , Mid : {mid} and Lo : {lo}")
        if elem == nums[mid]:
            return mid
        
        # [6, 7, 8, 1, 2, 3, 4, 5] elem = 2
        elif mid < hi and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1] :
            if elem < nums[mid-1] and elem >= nums[lo]:
                hi = mid-1
            else:
                lo = mid + 1
        elif elem >= nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1



if __name__ == '__main__':

    l = [6,6,7,8, 1, 2, 3, 4, 5, 6]
    l = [8,8,1,2,8]
    l= [6, 7, 8, 1, 2, 3, 4, 5]
    pos = get_pos_rotated_array(l, 6)
    print(pos)