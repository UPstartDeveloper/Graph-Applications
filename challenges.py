def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
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
        
