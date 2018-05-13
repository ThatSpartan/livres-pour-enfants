def BinarySearch(arr, val):

    if len(arr) == 0 or (len(arr) == 1 and arr[0][0] != val):
        return False

    mid_count = len(arr) // 2
    mid_val = arr[mid_count][0]

    print('Full Length : ' + str(len(arr)))
    print('Mid Length : ' + str(len(arr) // 2))
    print('Mid Length : ' + str(mid_count))
    print('Mid Val : ' + str(mid_val))

    if val == mid_val: # val is middle item
        return arr[mid_count][1]

    elif val < mid_val: # val is to the left (smaller)
        print(arr[:mid_count])
        return BinarySearch(arr[:mid_count], val)

    elif val > mid_val: # val is to the right (bigger)
        print(arr[mid_count+1:])        
        return BinarySearch(arr[mid_count+1:], val)

a = [[1, 'one'],[2, 'two'],[3, 'three'],[4, 'four'],[5, 'five'],[6, 'six'],[7, 'seven'],[8, 'eight'],[9, 'nine']]

print(BinarySearch(a, 3))
print('---------')
print(BinarySearch(a, 4))
print('---------')
print(BinarySearch(a, 5))
print('---------')
print(BinarySearch(a, 7))