def floor(arr,target):
    start = 0
    end = len(arr)-1
    while(start<end):
        mid = start+(end-start)//2
        if target>arr[mid]:
            start = mid+1
        elif target<arr[mid]:
            end  = mid -1
        else:
            return mid
    return mid # it should be end as per kunal but mid works for me
#print(floor(arr, target))
