def BinarySearch(arr,left,right,val):

    if left > right:
        return False

    mid = (left + right) // 2

    if arr[mid] == val:
        return True
    
    if val < arr[mid]:
        return BinarySearch(arr,left,mid-1,val)
    else:
        BinarySearch(arr,mid+1,right,val)

