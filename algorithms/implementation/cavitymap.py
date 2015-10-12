n = int(input())


## somewhat convoluted way to load the grid into memory but whatever
## it's n by n so whatever lol
grid = []
counter = 0
temp = ''
for i in range(n):
    temp += input()

# this is an array of strings of our input
grid = [temp[i:i+n] for i in range(0, len(temp), n)]

# convert it into a list of char arrays
grid = [list(i) for i in grid]


# look for cavities
for i in range(1,n-1):
    for j in range(1,n-1):
        curr = grid[i][j] 
        if curr > grid[i+1][j] and curr > grid[i][j+1] and curr > grid[i-1][j] and curr > grid[i][j-1]:
            grid[i][j] = 'X'

# join char arrays in the grid to have a list of strings again
grid = [''.join(i) for i in grid]

for line in grid:
    print(line)
