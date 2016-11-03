#!/usr/bin/python

from math import sqrt

# takes two tuples that are points on a grid
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# returns position of nearest "d" element in board nxn matix
def nearest_dirt_pos(x, y, board):
    min_distance = 9999.99
    min_point = (None, None)
    
    for i in range(len(board)):
        # assume square board CHECK THIS
        for j in range(len(board[i])):
            if board[i][j] is "d": 
                # check if this is a smaller distance than previous min.
                point_dist = euclidean_distance((x,y), (i,j))
                if float(point_dist) < float(min_distance):
                    # update min point
                    min_distance = point_dist
                    min_point    = (i,j)
    return min_point

           
def next_move(x, y, board):
    curr = board[x][y]
    
    if curr is "d":
        print("CLEAN")
        return
    
    target = nearest_dirt_pos(x, y, board)
    dx = target[0]
    dy = target[1]
    
    if (dx - x) > 0:
        print("DOWN")
        return
    elif (dx - x) < 0:
        print ("UP")
        return
    elif (dy - y) > 0:
        print("RIGHT")
        return
    else:
        print ("LEFT")
        return

if __name__ == "__main__":
    # get robot's initial position from STDIN
    pos = [int(i) for i in input().strip().split()]
    # get dimensions of world from STDIN
    dim = [int(i) for i in input().strip().split()]
    w, h = dim[0], dim[1]
    board = [[j for j in input().strip()] for i in range(w)]
    
    next_move(pos[0], pos[1], board)
