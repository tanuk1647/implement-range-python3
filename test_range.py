import unittest


def getitem(obj, index):
    return obj[index]


class RangeTests(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Range,)
        self.assertRaises(TypeError, Range, 1, 2, 3, 4)
        self.assertRaises(TypeError, Range, '1')
        
        class One():
            def __index__(self):
                return 1
        one = One()
        r = Range(one, one, one)
        self.assertEqual(r.start, 1)
        self.assertEqual(r.stop, 1)
        self.assertEqual(r.step, 1)
        
        r = Range(1)
        o = range(1)
        self.assertEqual(r.start, o.start)
        self.assertEqual(r.stop, o.stop)
        self.assertEqual(r.step, o.step)
        
        r = Range(1, 2)
        o = range(1, 2)
        self.assertEqual(r.start, o.start)
        self.assertEqual(r.stop, o.stop)
        self.assertEqual(r.step, o.step)
        
        r = Range(1, 2, 3)
        o = range(1, 2, 3)
        self.assertEqual(r.start, o.start)
        self.assertEqual(r.stop, o.stop)
        self.assertEqual(r.step, o.step)
        
        self.assertRaises(ValueError, Range, 1, 2, 0)
    
    def test_len(self):
        r = Range(0, 0)
        o = range(0, 0)
        self.assertEqual(len(r), len(o))
        
        r = Range(10, 0)
        o = range(10, 0)
        self.assertEqual(len(r), len(o))
        
        r = Range(0, 10, -1)
        o = range(0, 10, -1)
        self.assertEqual(len(r), len(o))
        
        r = Range(1, 12, 1)
        o = range(1, 12, 1)
        self.assertEqual(len(r), len(o))
        
        r = Range(1, 12, 4)
        o = range(1, 12, 4)
        self.assertEqual(len(r), len(o))
        
        r = Range(-6, 5, 1)
        o = range(-6, 5, 1)
        self.assertEqual(len(r), len(o))
        
        r = Range(-6, 5, 4)
        o = range(-6, 5, 4)
        self.assertEqual(len(r), len(o))
        
        r = Range(6, -5, -1)
        o = range(6, -5, -1)
        self.assertEqual(len(r), len(o))
        
        r = Range(6, -5, -4)
        o = range(6, -5, -4)
        self.assertEqual(len(r), len(o))
        
        r = Range(-1, -12, -1)
        o = range(-1, -12, -1)
        self.assertEqual(len(r), len(o))
        
        r = Range(-1, -12, -4)
        o = range(-1, -12, -4)
        self.assertEqual(len(r), len(o))
    
    def test_getitem_slice(self):
        r = Range(10)
        
        self.assertRaises(ValueError, getitem, r, slice(1, 2, 0))
        
        self.assertEqual(r[:], Range(10))
        self.assertEqual(r[::], Range(10))
        self.assertEqual(r[::1], Range(10))
        self.assertEqual(r[::2], Range(0, 10, 2))
        
        self.assertEqual(r[::-1], Range(9, -1, -1))
        self.assertEqual(r[::-2], Range(9, -1, -2))
        
        self.assertEqual(r[1:2], Range(1, 2))
        self.assertEqual(r[1:9], Range(1, 9))
        self.assertEqual(r[1:-1], Range(1, 9))
        
        self.assertEqual(r[-20:-1], Range(0, 9))
        self.assertEqual(r[-20:-19], Range(0, 0))
    
    def test_getitem(self):
        r = Range(0)
        self.assertRaises(IndexError, getitem, r, -1)
        self.assertRaises(IndexError, getitem, r, 0)
        self.assertRaises(IndexError, getitem, r, 1)
        
        r = Range(1)
        o = range(1)
        self.assertRaises(IndexError, getitem, r, -2)
        self.assertEqual(r[-1], o[-1])
        self.assertEqual(r[0], o[0])
        self.assertRaises(IndexError, getitem, r, 1)
        
        r = Range(1, 10)
        o = range(1, 10)
        self.assertEqual(r[5], o[5])
        
        r = Range(-5, 5)
        o = range(-5, 5)
        self.assertEqual(r[2], o[2])
        self.assertEqual(r[7], o[7])
        
        r = Range(5, -5, -1)
        o = range(5, -5, -1)
        self.assertEqual(r[2], o[2])
        self.assertEqual(r[7], o[7])
        
        r = Range(-1, -10, -1)
        o = range(-1, -10, -1)
        self.assertEqual(r[5], o[5])
        
        r = Range(10)
        self.assertRaises(TypeError, getitem, r, '1')
    
    def test_bool(self):
        r = Range(10)
        o = range(10)
        self.assertEqual(bool(r), bool(o))
        
        r = Range(0)
        o = range(0)
        self.assertEqual(bool(r), bool(o))
    
    def test_repr(self):
        self.assertEqual(repr(Range(1)), 'Range(0, 1)')
        self.assertEqual(repr(Range(1, 2)), 'Range(1, 2)')
        self.assertEqual(repr(Range(1, 2, 3)), 'Range(1, 2, 3)')
    
    def test_eq(self):
        self.assertFalse(Range(10) == range(10))
        self.assertTrue(Range(1, 2, 3) == Range(1, 2, 3))
        self.assertFalse(Range(4, 2, 3) == Range(1, 2, 3))
        self.assertFalse(Range(1, 4, 3) == Range(1, 2, 3))
        self.assertFalse(Range(1, 2, 4) == Range(1, 2, 3))
    
    def test_ne(self):
        self.assertTrue(Range(10) != range(10))
        self.assertFalse(Range(1, 2, 3) != Range(1, 2, 3))
        self.assertTrue(Range(4, 2, 3) != Range(1, 2, 3))
        self.assertTrue(Range(1, 4, 3) != Range(1, 2, 3))
        self.assertTrue(Range(1, 2, 4) != Range(1, 2, 3))
    
    def test_hash(self):
        self.assertEqual(hash(Range(1)), hash(Range(0, 1, 1)))
    
    def test_iter_basic(self):
        self.assertEqual(
            [x for x in Range(0)],
            [x for x in range(0)])
        
        self.assertEqual(
            [x for x in Range(1)],
            [x for x in range(1)])
        
        self.assertEqual(
            [x for x in Range(3)],
            [x for x in range(3)])
        
        self.assertEqual(
            [x for x in Range(1, 10, 3)],
            [x for x in range(1, 10, 3)])
        
        self.assertEqual(
            [x for x in Range(-5, 5, 3)],
            [x for x in range(-5, 5, 3)])
        
        self.assertEqual(
            [x for x in Range(5, -5, -3)],
            [x for x in range(5, -5, -3)])
        
        self.assertEqual(
            [x for x in Range(-1, -10, -3)],
            [x for x in range(-1, -10, -3)])
        
        iterator = iter(Range(5))
        self.assertIs(iterator, iter(iterator))
    
    def test_reversed(self):
        self.assertEqual(
            [x for x in reversed(Range(1, 10, 3))],
            [x for x in reversed(range(1, 10, 3))])
        
        self.assertEqual(
            [x for x in reversed(Range(-5, 5, 3))],
            [x for x in reversed(range(-5, 5, 3))])
        
        self.assertEqual(
            [x for x in reversed(Range(5, -5, -3))],
            [x for x in reversed(range(5, -5, -3))])
        
        self.assertEqual(
            [x for x in reversed(Range(-1, -10, -3))],
            [x for x in reversed(range(-1, -10, -3))])
    
    def test_contains(self):
        r = Range(1, 10, 1)
        self.assertNotIn(0, r)
        self.assertIn(1, r)
        self.assertIn(9, r)
        self.assertNotIn(10, r)
        
        r = Range(1, 10, 3)
        self.assertNotIn(-2, r)
        self.assertIn(1, r)
        self.assertNotIn(2, r)
        self.assertIn(7, r)
        self.assertNotIn(9, r)
        self.assertNotIn(10, r)
        
        r = Range(-5, 5, 1)
        self.assertNotIn(-6, r)
        self.assertIn(-3, r)
        self.assertIn(0, r)
        self.assertIn(3, r)
        self.assertNotIn(5, r)
        
        r = Range(-5, 5, 3)
        self.assertNotIn(-8, r)
        self.assertIn(-5, r)
        self.assertNotIn(-4, r)
        self.assertNotIn(-3, r)
        self.assertIn(-2, r)
        self.assertNotIn(-1, r)
        self.assertNotIn(0, r)
        self.assertIn(1, r)
        self.assertNotIn(2, r)
        self.assertNotIn(3, r)
        self.assertIn(4, r)
        self.assertNotIn(5, r)
        self.assertNotIn(7, r)
        
        r = Range(5, -5, -1)
        self.assertNotIn(6, r)
        self.assertIn(3, r)
        self.assertIn(0, r)
        self.assertIn(-3, r)
        self.assertNotIn(-5, r)
        
        r = Range(5, -5, -3)
        self.assertNotIn(8, r)
        self.assertIn(5, r)
        self.assertNotIn(4, r)
        self.assertNotIn(3, r)
        self.assertIn(2, r)
        self.assertNotIn(1, r)
        self.assertNotIn(0, r)
        self.assertIn(-1, r)
        self.assertNotIn(-2, r)
        self.assertNotIn(-3, r)
        self.assertIn(-4, r)
        self.assertNotIn(-5, r)
        self.assertNotIn(-7, r)
        
        r = Range(-1, -10, -1)
        self.assertNotIn(0, r)
        self.assertIn(-1, r)
        self.assertIn(-9, r)
        self.assertNotIn(-10, r)
        
        r = Range(-1, -10, -3)
        self.assertNotIn(2, r)
        self.assertIn(-1, r)
        self.assertNotIn(-2, r)
        self.assertIn(-7, r)
        self.assertNotIn(-9, r)
        self.assertNotIn(-10, r)
    
    def test_count(self):
        r = Range(1, 10)
        self.assertEqual(r.count(9), 1)
        self.assertEqual(r.count(10), 0)
        
        r = Range(1, 10, 3)
        self.assertEqual(r.count(7), 1)
        self.assertEqual(r.count(9), 0)

        r = Range(-5, 5)
        self.assertEqual(r.count(4), 1)
        self.assertEqual(r.count(5), 0)
        
        r = Range(-5, 5, 3)
        self.assertEqual(r.count(4), 1)
        self.assertEqual(r.count(5), 0)
        
        r = Range(5, -5, -1)
        self.assertEqual(r.count(-4), 1)
        self.assertEqual(r.count(-5), 0)
        
        r = Range(5, -5, -3)
        self.assertEqual(r.count(-4), 1)
        self.assertEqual(r.count(-5), 0)
        
        r = Range(-1, -10, -1)
        self.assertEqual(r.count(-9), 1)
        self.assertEqual(r.count(-10), 0)
        
        r = Range(-1, -10, -3)
        self.assertEqual(r.count(-7), 1)
        self.assertEqual(r.count(-9), 0)
    
    def test_index(self):
        r = Range(1, 10, 1)
        o = range(1, 10, 1)
        self.assertRaises(ValueError, r.index, 0)
        self.assertEqual(r.index(1), o.index(1))
        self.assertEqual(r.index(9), o.index(9))
        self.assertRaises(ValueError, r.index, 10)
        
        r = Range(1, 10, 3)
        o = range(1, 10, 3)
        self.assertRaises(ValueError, r.index, -2)
        self.assertEqual(r.index(1), o.index(1))
        self.assertRaises(ValueError, r.index, 2)
        self.assertEqual(r.index(7), o.index(7))
        self.assertRaises(ValueError, r.index, 9)
        self.assertRaises(ValueError, r.index, 10)
        
        r = Range(-5, 5, 1)
        o = range(-5, 5, 1)
        self.assertRaises(ValueError, r.index, -6)
        self.assertEqual(r.index(-3), o.index(-3))
        self.assertEqual(r.index(0), o.index(0))
        self.assertEqual(r.index(3), o.index(3))
        self.assertRaises(ValueError, r.index, 5)
        
        r = Range(-5, 5, 3)
        o = range(-5, 5, 3)
        self.assertRaises(ValueError, r.index, -8)
        self.assertEqual(r.index(-5), o.index(-5))
        self.assertRaises(ValueError, r.index, -4)
        self.assertRaises(ValueError, r.index, -3)
        self.assertEqual(r.index(-2), o.index(-2))
        self.assertRaises(ValueError, r.index, -1)
        self.assertRaises(ValueError, r.index, 0)
        self.assertEqual(r.index(1), o.index(1))
        self.assertRaises(ValueError, r.index, 2)
        self.assertRaises(ValueError, r.index, 3)
        self.assertEqual(r.index(4), o.index(4))
        self.assertRaises(ValueError, r.index, 5)
        self.assertRaises(ValueError, r.index, 7)
        
        r = Range(5, -5, -1)
        o = range(5, -5, -1)
        self.assertRaises(ValueError, r.index, 6)
        self.assertEqual(r.index(3), o.index(3))
        self.assertEqual(r.index(0), o.index(0))
        self.assertEqual(r.index(-3), o.index(-3))
        self.assertRaises(ValueError, r.index, -5)
        
        r = Range(5, -5, -3)
        o = range(5, -5, -3)
        self.assertRaises(ValueError, r.index, 8)
        self.assertEqual(r.index(5), o.index(5))
        self.assertRaises(ValueError, r.index, 4)
        self.assertRaises(ValueError, r.index, 3)
        self.assertEqual(r.index(2), o.index(2))
        self.assertRaises(ValueError, r.index, 1)
        self.assertRaises(ValueError, r.index, 0)
        self.assertEqual(r.index(-1), o.index(-1))
        self.assertRaises(ValueError, r.index, -2)
        self.assertRaises(ValueError, r.index, -3)
        self.assertEqual(r.index(-4), o.index(-4))
        self.assertRaises(ValueError, r.index, -5)
        self.assertRaises(ValueError, r.index, -7)

        r = Range(-1, -10, -1)
        o = range(-1, -10, -1)
        self.assertRaises(ValueError, r.index, 0)
        self.assertEqual(r.index(-1), o.index(-1))
        self.assertEqual(r.index(-9), o.index(-9))
        self.assertRaises(ValueError, r.index, -10)
        
        r = Range(-1, -10, -3)
        o = range(-1, -10, -3)
        self.assertRaises(ValueError, r.index, 2)
        self.assertEqual(r.index(-1), o.index(-1))
        self.assertRaises(ValueError, r.index, -2)
        self.assertEqual(r.index(-7), o.index(-7))
        self.assertRaises(ValueError, r.index, -9)
        self.assertRaises(ValueError, r.index, -10)
    
    def test_large_nums(self):
        import sys
        ln = sys.maxsize + 1
        r = Range(ln, 3*ln, 1)
        o = range(ln, 3*ln, 1)
        self.assertEqual(r._len, 2*ln)
        self.assertEqual(r[0], o[0])
        self.assertEqual(r[-1], r[-1])
        self.assertIn(2*ln, r)
        self.assertEqual(r.count(2*ln), 1)
        self.assertEqual(r.index(2*ln), o.index(2*ln))


if __name__ == '__main__':
    from range import Range
    unittest.main()
