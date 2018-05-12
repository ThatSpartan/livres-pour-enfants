livre = [None] * 14
livre[0] = [2,"Pinocchio"]
livre[1] = [5,"Maria Chapdelaine"]
livre[2] = [7,"L'Homme invisible"]
livre[3] = [10,"Contes fantastiques"]
livre[4] = [13,"L'Assassin habite au 21"]
livre[5] = [17,"L'Agent secret"]
livre[6] = [22,"Robinson Crusoe"]
livre[7] = [25,"Les aventures d'Alice au pays des merveilles"]
livre[8] = [29,"Voyage au centre de la terre"]
livre[9] = [30,"Famille suisse Robinson"]
livre[10] = [31,"Trois mousquetaires"]
livre[11] = [35,"Aurélia"]
livre[12] = [36,"Les deux orphelines"]
livre[13] = [40,"Le joueur"]

a = [1,2,3,4,5,6,7,8,9]

def binary_search(arr, val):
    
    print(type(val))

    for x in livre:
        print(str(x[0]) + ' : ' + x[1])

    if len(arr) == 0 or (len(arr) == 1 and arr[0][0] != val):
        # return False
        return None

    mid = arr[len(arr)//2][0] # value at the middle of the array

    if val == mid:  return mid
    if val < mid:   return binary_search( arr[:len(arr) // 2        ], val)
    if val > mid:   return binary_search( arr[len(arr)  // 2 + 1:   ], val)

if __name__ == '__main__':

    while True:
        ask_user = input('Input ref # : ')
        try:
            print(livre[binary_search(livre, int(ask_user))])
        except ValueError:
            print('Error 101 : Please input a reference number')
        
