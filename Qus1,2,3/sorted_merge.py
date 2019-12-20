
def mergeArrays(arr1, arr2, n1, n2): 
	arr3 = [None] * (n1 + n2) 
	i = 0
	j = 0
	k = 0

	while i < n1 and j < n2: 

		if arr1[i] < arr2[j]: 
			arr3[k] = arr1[i] 
			k = k + 1
			i = i + 1
		else: 
			arr3[k] = arr2[j] 
			k = k + 1
			j = j + 1

	while i < n1: 
		arr3[k] = arr1[i]; 
		k = k + 1
		i = i + 1

	while j < n2: 
		arr3[k] = arr2[j]; 
		k = k + 1
		j = j + 1
	print("Resut of merging") 
	for i in range(n1 + n2): 
		print(str(arr3[i]), end = " ") 

arr1 = [2, 4, 6, 12] 
n1 = len(arr1) 

arr2 = [0, 9, 10, 13] 
n2 = len(arr2) 
mergeArrays(arr1, arr2, n1, n2); 

