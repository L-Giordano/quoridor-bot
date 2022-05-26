import unittest
from src.player import wall


class Test_wall(unittest.TestCase):

    # orientation w
    def test_find_edges_W_to_remove(self):
        expected = [((2, 3), (2, 2)), ((1, 3), (1, 2)), ((3, 3), (3, 2))]
        result = wall.find_edges_to_remove(2, 2, 2, 3, 'w')
        print(result)
        self.assertEqual(result, expected)

    # orientation s
    def test_find_edges_S_to_remove(self):
        expected = [((2, 2), (1, 2)), ((2, 1), (1, 1)), ((2, 3), (1, 3))]
        result = wall.find_edges_to_remove(2, 2, 1, 2, 's')
        self.assertEqual(result, expected)

    def test_wall_coor(self):
        expected = ['h', 2, 1]
        result = wall.wall_coor([((2, 2), (1, 2)), ((2, 1), (1, 1))])
        self.assertEqual(result, expected)

    # Must test:
    # remove_egde
    # verify_wall
