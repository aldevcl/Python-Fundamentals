arr = [1,5,3,2,0,8]

def bubblesort(arr):
    count = 0
    print(arr, "\n")
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            count += 1
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
    print('# de evaluaciones', count)
    return arr

print(bubblesort(arr))