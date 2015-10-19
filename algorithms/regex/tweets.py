n = int(input())

count = 0 

for x in range(n):
    temp = str(input()).lower()

    if 'hackerrank' in temp:
        count += 1
        
print(count)
