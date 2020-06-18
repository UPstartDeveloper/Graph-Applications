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
        print(f'Queue to start: {queue}, minutes = {minutes}')
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
                # make sure elements are true neighbors
                try:
                    # no negative indexing allowed
                    if 0 <= x_p < len(grid) and 0 <= y_p < len(grid[0]): 
                        if grid[x_p][y_p] == 1 and (x_p, y_p) not in visited:
                            queue.append((x_p, y_p))
                except IndexError:
                    pass
            # visit the orange
            queue.remove((x, y))
            visited.add((x, y))
        # increment minutes
        minutes += 1
    # if 1's still remain, then return -1
    for x, row in enumerate(grid):
        for y, val, in enumerate(row):
            if grid[x][y] == 1:
                print('ones remain!')
                return -1
    # else return minutes
    return minutes


def dfs_for_cc(grid, point, visited, island):
    """Returns a list of all vertices within one island.

        Parameters:
        point(tuple): the coordinates of the starting point
        visited(set): all other points visited in the overall grid so far
        connected(list): collection of points visted so far in this
                         single distinct land mass

        Returns: list: all point within one distinct land mass
    
    """
    # visit this vertex
    visited.add(point)
    # iterate over neighbors
    x, y = point
    neighbors = (
        (x, y - 1),  # left
        (x, y + 1),  # right
        (x - 1, y),  # up
        (x + 1, y)  # down
    )
    for neighbor_coordinates in neighbors:
        # get the coordinates of the neighbor
        neighbor_x, neighbor_y = neighbor_coordinates
        # prevent negative indexing
        if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
            value = grid[neighbor_x][neighbor_y]
            if value == 1 and neighbor_coordinates not in visited:
                dfs_for_cc(grid, neighbor_coordinates, visited, island)
            # now all neighbors visited - this point can be included as well
            island.append(point)
    return None

def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands.
       Idea 1: each island is a set of connected components in the overall grid
    
    """
    # init a list of distinct land masses
    islands = list()
    # set for all previously seen points
    visited = set()
    # execute DFS - find all connected components
    for x, row in enumerate(grid):
        for y, grid_val in enumerate(row):
            if grid_val == 1 and (x, y) not in visited:
                island = list()
                # perform DFS, update the points visited
                dfs_for_cc(grid, (x, y), visited, island)
                # if repeat points visited, list is empty
                if len(island) > 0:
                    islands.append(island)
    # return the number of islands
    return len(islands)

def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain
       from beginWord to endWord, using words from wordList.
    
    """
    pass


if __name__ == "__main__":
    pass

