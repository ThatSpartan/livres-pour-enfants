def BinarySearch(arr, val):

    """ Binary Search Function
    
    Returns:
        String -- Should return the name of the book searched
    """


    if len(arr) == 0 or (len(arr) == 1 and arr[0][0] != val):
        return False

    mid_count = len(arr) // 2
    mid_val = arr[mid_count][0]

    if val == mid_val: # val is middle item
        return arr[mid_count][1]

    elif val < mid_val: # val is to the left (smaller)
        print(arr[:mid_count])
        return BinarySearch(arr[:mid_count], val)

    elif val > mid_val: # val is to the right (bigger)
        print(arr[mid_count+1:])        
        return BinarySearch(arr[mid_count+1:], val)
