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

def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    # init a counter for the number of land masses
    islands = 0
    # Idea 1: each island is a set of connected components in the overall grid
    # return the number of islands
    return islands


if __name__ == "__main__":
    pass


# code for using DFS to find all CC from before
def dfs_for_cc(self, vertex, visited, connected):
    """Returns a list of all verticies within one set of
        connected components in a Graph object.

        Parameters:
        vertex(Vertex): the vertex we begin with
        visited(set): all other Vertex objects visited in the overall
                        graph so far
        connected(list): collection of vertices visted so far in this
                        set of connected components

        Returns: list: all verticies within one set of
        connected components in a graph
    
    """
    # visit this vertex
    visited.add(vertex)
    connected.append(vertex.get_id())
    # iterate over neighbors
    neighbors = vertex.get_neighbors()
    for n in neighbors:
        if n not in visited:
            self.dfs_for_cc(n, visited, connected)
    return connected

def find_connected_components(self):
    """Return a 2D list of connected components.
        Each of the inner lists contains vertex ids.
        A connected component of a graph is a set
        of vertices for which there is a path between any pair of vertices.

    """
    # set for all previous seen vertices
    visited = set()
    # execute DFS - find all connected components
    all_connected_components = list()
    for vertex in self.__vertex_dict.values():
        if vertex not in visited:
            components = list()
            self.dfs_for_cc(vertex, visited, components)
            all_connected_components.append(components)
    # return the connected components
    return all_connected_components