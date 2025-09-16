import unittest
from pa1 import create_adj_list, dijkstra

class TestCreateAdjList(unittest.TestCase):
    def test_empty(self):
        E = []
        V = []
        expected = {}
        self.assertEqual(create_adj_list(E, V), expected)

    def test_one_edge(self):
        E = [(0, 0, 0, 1, 1)]
        V = [(0, 0), (0, 1)]
        expected = {
            (0, 0): [((0, 1), 1)], 
            (0, 1): [((0,0), 1)]
            }
        self.assertEqual(create_adj_list(E, V), expected)
    
    def test_two_edges(self):
        E = [(0, 0, 0, 1, 1), (0, 0, 1, 0, 1)]
        V = [(0, 0), (0, 1), (1, 0)]
        expected = {
            (0, 0): [((0, 1), 1), ((1, 0), 1)], 
            (0, 1): [((0,0), 1)],
            (1, 0): [((0,0), 1)]
        }
        self.assertEqual(create_adj_list(E, V), expected)

    def test_duplicate_edges(self):
        E = [(0, 0, 0, 1, 1), (0, 0, 0, 1, 1)]
        V = [(0, 0), (0, 1)]
        expected = {
            (0, 0): [((0, 1), 1)], 
            (0, 1): [((0,0), 1)]
        }
        self.assertEqual(create_adj_list(E, V), expected)



if __name__ == '__main__':
    unittest.main()