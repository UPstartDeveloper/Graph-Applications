def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    # init variables
    minutes = -1
    visited = set()
    queue = list()
    # enqueue the first rotten orange
    for x, row in enumerate(grid):
        for y, val, in enumerate(row):
            if grid[x][y] == 2:
                queue.append((x, y))
    # if none found, then return -1
    if len(queue) == 0:
        return minutes
    # execute BFS
    while len(queue) > 0:
        # visit all the oranges to rot during this minute
        rotten_this_min = list()
        for (x, y) in queue.copy():
            # make the orange rotten rotten
            if grid[x][y] == 1:
                grid[x][y] = 2
                rotten_this_min.append((x, y))
            # add the neighbors of this orange
            potentials = [
                (x, y - 1),  # left
                (x, y + 1),  # right
                (x - 1, y),  # up
                (x + 1, y)  # down
            ]
            for (x_p, y_p) in potentials:
                # make sure elements are true neighbors, not negative indexing
                try:
                    if 0 <= x_p <= len(grid) and 0 <= y_p <= len(grid[x_p]): 
                        if grid[x_p][y_p] == 1 and (x_p, y_p) not in visited:
                            queue.append((x_p, y_p))
                except IndexError:
                    pass
        # remove all the oranges that rot this min
        for orange in rotten_this_min:
            queue.remove(orange)
            visited.add(orange)
        # on first iterationm remove the initially rotten
        else:
            visited.add(queue.pop(0))
        # increment min
        minutes += 1
    # if 1's still remain, then return -1
    for x, row in enumerate(grid):
        for y, val, in enumerate(row):
            if grid[x][y] == 1:
                return -1
    # else return minutes
    return minutes


if __name__ == "__main__":
    oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
# minutes = timeToRot(oranges1)
# print(minutes)
# assert minutes == 4, f'Minutes: {minutes}'
# additional tests
oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
# assert timeToRot(oranges2) == -1

oranges3 = [
    [0,2]
]
assert timeToRot(oranges3) == 0
     
        
