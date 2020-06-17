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
    # init_rotten = list()
    for x, row in enumerate(grid):
        for y, val, in enumerate(row):
            if grid[x][y] == 2:
                queue.append((x, y))
    # if none found, then return -1
    if len(queue) == 0:
        return minutes
    # execute BFS
    # queue.append(init_rotten.pop)
    # print(f'Qeue before BFS: {queue}')
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
                (x, y - 1),  # up
                (x, y + 1),  # down
                (x - 1, y),  # left
                (x + 1, y)  # right
            ]
            for (x_p, y_p) in potentials:
                try:
                    if grid[x_p][y_p] == 1 and (x_p, y_p) not in visited:
                        queue.append((x_p, y_p))
                        # visited.add((x_p, y_p))
                except IndexError:
                    continue
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
                print("1's remaining!")
                return -1
    # else return minutes
    return minutes
                        
    """
    # init a set of rotten oranges
    visited = set()  # stores xy coordinates
    # init queue
    queue = list()
    # Step 1: find the first rotten orange
    # A: iterate over the elements, and find the first rotten orange (2)
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            # if it is found --> enqueue (x, y) in the queue
            if value == 2:
                queue.append((x, y))
    # init a minutes count, to incrmement during BFS
    minutes = -1
    # Step 2: perform BFS
    while len(queue) > 0:
        # dequeue orange from the queue
        x, y = queue.pop(0)
        orange = grid[x][y]
        # "visit" - if the orange is fresh (1), then make it rotten (2)
        if orange == 1:
            grid[x][y] = 2
        visited.add((x, y))
        # calculate (x, y)'s of potential neighbors
        potentials = [
            (x, y - 1),  # up
            (x, y + 1),  # down
            (x - 1, y),  # left
            (x + 1, y),  # right
        ]
        # check if the potential is a fresh orange
        for potential in potentials:
            try:
                x, y = potential
                potential_orange = grid[x][y]
                # enqueue those coordinates if so
                if potential_orange == 1 and (x, y) not in visited:
                    queue.append((x, y))
            except IndexError:
                break
        # increment minutes
        minutes += 1
    # Step 3: return minutes
    return minutes
    """

if __name__ == "__main__":
    oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
minutes = timeToRot(oranges1)
# print(minutes)
assert minutes == 4, f'Minutes: {minutes}'
# additional tests
oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0,2]
]
assert timeToRot(oranges3) == 0
     
        
