def time_to_rot(grid):
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
        for y, value, in enumerate(row):
            if value == 2:
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

def num_islands(grid):
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

def course_order(num_courses, prerequisites):
    """Return a course schedule according to the prerequisites provided.
       Utilizes topological sort, using Kahn's Algorithm.

    """
    # A: calculate the in-degree of each course (a vertex)
    course_in_degrees = dict()
    for course_pair in prerequisites:
        course, prereq = course_pair
        # map the in-degrees of the course
        course_in_degree = 1
        if course in course_in_degrees:
            course_in_degree += course_in_degrees[course]
        course_in_degrees[course] = course_in_degree
        # map the in degree of the prereq
        if prereq not in course_in_degrees:
            course_in_degrees[prereq] = 0
    # B: find a valid course order
    course_order = list()
    while len(course_in_degrees) > 0:
        # C: find  a course with in-degree of 0
        next_course = None
        for course in course_in_degrees:
            if course_in_degrees[course] == 0:
                next_course = course
        # add to solution
        course_order.append(next_course)
        # remove from the set of courses to take
        del course_in_degrees[next_course]
        # D: decrement the in-degree of the following course
        # iterate over course pairings
        for course_pair in prerequisites:
            # find each pair where next_course found
            course, prereq = course_pair
            if next_course == prereq:
                # go in the dict and decrement the value
                course_in_degrees[course] -= 1
    return course_order


def word_ladder_length(begin_word, end_word, word_list):
    """Return the length of the shortest word chain
       from beginWord to endWord, using words from wordList.
    
    """
    # make sure the transformation is possible
    assert len(begin_word) == len(end_word) and end_word in word_list
    # store a dict of all words and their neighbors
    word_list.append(begin_word)
    word_neighbors = dict()
    for index, word, in enumerate(word_list):
        neighbors = list()
        # check the differences in spelling between words
        for other_index, other_word in enumerate(word_list):
            diff = set(word) - set(other_word)  # letters in word, not in other
            if len(diff) == 1:
                neighbors.append(other_word)
        # add pair to dict
        word_neighbors[word] = neighbors
    # use BFS to get from beginWord to the end
    queue = [begin_word]
    # visited = set()
    # store each word, with path taken from beginWord to reach it
    word_path = {
        begin_word: [begin_word]
    }
    while len(queue) > 0:
        current_word = queue.pop()

        # found the end
        if current_word == end_word:
            break
        
        # enqueue the neighbors
        neighbors = word_neighbors[current_word]
        for neighbor in neighbors:
            if neighbor not in word_path:
                current_path = word_path[current_word]
                # extend the path by 1 word
                next_path = current_path + [neighbor]
                word_path[neighbor] = next_path
                queue.append(neighbor)
    # return the length
    return len(word_path[end_word])
