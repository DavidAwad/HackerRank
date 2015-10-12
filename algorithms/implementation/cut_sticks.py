n = int(input())

# list comprehensions :D 
sticks = [int(s) for s in input().split()]

# we're going to be making n cuts
for i in range(n):
    if not sticks:
        break
    cut = min(sticks)
    # make a cut across all sticks by that length
    sticks = [x - cut for x in sticks]
    print(len(sticks))
    # filter out sticks with 0 length
    sticks = list(filter(lambda x: x > 0, sticks))
