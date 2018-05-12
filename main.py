def Search(arr,val):

    if len(arr)==0 or (len(arr)==1 and arr[0]!=val):
        return False

    print('Full Array : ' + str(arr))

    mid=arr[len(arr)//2]

    print('Mid Point : ' + str(mid))

    if val==mid:    return True
    if val<mid:     return Search(arr[:len(arr)//2],val)
    if val>mid:     return Search(arr[len(arr)//2+1:],val)

a=[1,2,3,4,5,6,7,8,9]

print(Search(a,4))
print(Search(a,8))