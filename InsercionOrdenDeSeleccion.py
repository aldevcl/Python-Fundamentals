x = [8,5,2,6,9,3,1,4,0,7]

def insert_sort(arr): 
	for i in range(1, len(arr)):
		insert = i
		temp = arr[i]
		for j in range(0, i): 
			if temp < arr[i - 1 - j]: 
				arr[i - j] = arr[i - 1 - j]
				insert = i - 1 - j
		if insert != i:
			arr[insert] = temp
	return arr

print(insert_sort(x))