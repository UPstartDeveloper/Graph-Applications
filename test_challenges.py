import challenges
import unittest

class RottingOrangesTests(unittest.TestCase):
    def test_timeToRot(self):
        """
        Graph BFS problem. Tells the time taken for oranges to all rot.
        Test cases from LeetCode.
        """
        # Test Cases
        oranges1 = [
            [2,1,1],
            [1,1,0],
            [0,1,1]
        ]
        assert challenges.timeToRot(oranges1) == 4

        oranges2 = [
            [2,1,1],
            [0,1,1],
            [1,0,1]
        ]
        assert challenges.timeToRot(oranges2) == -1

        oranges3 = [
            [0,2]
        ]
        assert challenges.timeToRot(oranges3) == 0

    def test_numIslands(self):
        '''Returns the number of distinct land masses from a 2D grid.'''
        # Test Cases
        map1 = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        # assert challenges.numIslands(map1) == 1

        map2 = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        assert challenges.numIslands(map2) == 3


if __name__ == '__main__':
    unittest.main()