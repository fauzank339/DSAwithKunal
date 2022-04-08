#A function for a Simple Binary Search 
#Complexity O(log n)
def binarySearch(arr, target):
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
    return -1

''' Binary Search is the best searching algorith we have. It is very similar to how we search in a dictionary
    First we find the middle position, then we check wheather our object of interest is preent threre, if yes then
    we consider that we have achieved our goal and return that position, else we search in lower half or upper half
    depending on wheather the object is most likey to be found in above half or lower half. there is usually a pre defined condition for it,
    We keep repeating this proces until we find what we are looking for or we dont.
