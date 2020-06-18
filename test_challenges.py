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


class NumIslandsTests(unittest.TestCase):
    def test_numIslands(self):
        '''Returns the number of distinct land masses from a 2D grid.'''
        # Test Cases
        map1 = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        assert challenges.numIslands(map1) == 1

        map2 = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        assert challenges.numIslands(map2) == 3


class ClassSchedulingTests(unittest.TestCase):
    def test_courseOrder(self):
        """Returns the order in which courses must be taken,
           in order to meet prerequisites.
        
        """
        courses1 = [ [1,0] ]
        assert challenges.courseOrder(2, courses1) == [0, 1]

        courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
        possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
        assert challenges.courseOrder(4, courses2) in possibleSchedules

class WordLadderTests(unittest.TestCase):
    def test_wordLadderLength(self):
        """Returns the minimum amount of 1-letter transformations to change
           one word to another.

        """
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]

        assert challenges.wordLadderLength(beginWord, endWord, wordList) == 5



if __name__ == '__main__':
    unittest.main()