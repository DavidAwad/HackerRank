n = int(input())

for i in range(n):
    m = int(input().split()[1])
    arr = [int(x) for x in input().split()]

    subarrays = [] 
    
    # create larger and larger sub-arrays
    for i in range(len(arr)):
       yolo = [subarrays.append(arr[j:j+i]) for j in range(len(arr))]
    
    subarrays.append(arr)
    subarray_mods = [sum(x)%m for x in subarrays]
    
    print(max(subarray_mods))
