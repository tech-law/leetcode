def get_element_position(nums, elem):
    
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2   
        if elem == nums[mid]:
            if mid > 0 and elem == nums[mid-1]:
                hi = mid
            else:
                return mid
        elif elem > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

def get_element_position_right(nums, elem):
    
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2   
        if elem == nums[mid]:
            if mid < hi and elem == nums[mid+1]:
                lo = mid
            else:
                return mid
        elif elem > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5,5,5,5, 6, 7 ,8 ,9,9,9,9, 10]
    e = 7

    position = get_element_position(l, 5) 

    print(position)
    

    position = get_element_position_right(l, 5) 

    print(position)
    