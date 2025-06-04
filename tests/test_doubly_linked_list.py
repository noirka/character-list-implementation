import unittest
from src.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
    
    def test_initial_state(self):
        self.assertEqual(self.list.length(), 0)
    
    def test_append(self):
        self.list.append('A')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'A')
        
        self.list.append('B')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(1), 'B')
    
    def test_insert(self):
        self.list.insert('A', 0)
        self.assertEqual(self.list.to_list(), ['A'])
        
        self.list.insert('B', 0)
        self.assertEqual(self.list.to_list(), ['B', 'A'])
        
        self.list.insert('C', 1)
        self.assertEqual(self.list.to_list(), ['B', 'C', 'A'])
        
        self.list.insert('D', 3)
        self.assertEqual(self.list.to_list(), ['B', 'C', 'A', 'D'])
        
        with self.assertRaises(IndexError):
            self.list.insert('X', -1)
        with self.assertRaises(IndexError):
            self.list.insert('X', 5)
    
    def test_delete(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('C')
        
        self.assertEqual(self.list.delete(1), 'B')
        self.assertEqual(self.list.to_list(), ['A', 'C'])
        
        self.assertEqual(self.list.delete(0), 'A')
        self.assertEqual(self.list.to_list(), ['C'])
        
        self.assertEqual(self.list.delete(0), 'C')
        self.assertEqual(self.list.length(), 0)
        
        with self.assertRaises(IndexError):
            self.list.delete(0)
    
    def test_deleteAll(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('A')
        self.list.append('C')
        self.list.append('A')
        
        self.list.deleteAll('A')
        self.assertEqual(self.list.to_list(), ['B', 'C'])
        self.assertEqual(self.list.length(), 2)
        
        self.list.deleteAll('X')
        self.assertEqual(self.list.to_list(), ['B', 'C'])
    
    def test_get(self):
        self.list.append('A')
        self.list.append('B')
        
        self.assertEqual(self.list.get(0), 'A')
        self.assertEqual(self.list.get(1), 'B')
        
        with self.assertRaises(IndexError):
            self.list.get(-1)
        with self.assertRaises(IndexError):
            self.list.get(2)
    
    def test_clone(self):
        self.list.append('A')
        self.list.append('B')
        
        clone = self.list.clone()
        self.assertEqual(clone.to_list(), ['A', 'B'])
        
        clone.append('C')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(clone.length(), 3)
    
    def test_reverse(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('C')
        
        self.list.reverse()
        self.assertEqual(self.list.to_list(), ['C', 'B', 'A'])
        
        empty = DoublyLinkedList()
        empty.reverse()
        self.assertEqual(empty.length(), 0)
    
    def test_find(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('A')
        self.list.append('C')
        
        self.assertEqual(self.list.findFirst('A'), 0)
        self.assertEqual(self.list.findFirst('B'), 1)
        self.assertEqual(self.list.findFirst('X'), -1)
        
        self.assertEqual(self.list.findLast('A'), 2)
        self.assertEqual(self.list.findLast('C'), 3)
        self.assertEqual(self.list.findLast('X'), -1)
    
    def test_clear(self):
        self.list.append('A')
        self.list.append('B')
        self.list.clear()
        
        self.assertEqual(self.list.length(), 0)
        self.assertEqual(self.list.to_list(), [])
    
    def test_extend(self):
        self.list.append('A')
        
        other = DoublyLinkedList()
        other.append('B')
        other.append('C')
        
        self.list.extend(other)
        self.assertEqual(self.list.to_list(), ['A', 'B', 'C'])
        
        other.append('D')
        self.assertEqual(self.list.length(), 3)
        
        with self.assertRaises(TypeError):
            self.list.extend([1, 2, 3])
    
    def test_edge_cases(self):
        self.list.append('X')
        self.assertEqual(self.list.delete(0), 'X')
        self.assertEqual(self.list.length(), 0)
        
        self.list.append('Y')
        self.list.reverse()
        self.assertEqual(self.list.get(0), 'Y')

if __name__ == '__main__':
    unittest.main()