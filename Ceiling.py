#print(binarySearch(arr, target))
# ceiling in a sorted array
def ceiling(arr,target):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = start+(end-start)//2
        if target>arr[mid]:
            start = mid+1
        elif target<arr[mid]:
            end  = mid -1
        else:
            return mid
    return start

Algorithm= It is the same as binary Search except for return start at the end
That is because at that moment when condition fails start is greater that end and points
to the next element.
