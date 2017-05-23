from unittest import TestCase


class TestMerge_into(TestCase):
    def test_merge_into(self):
        try:
            from build import merge_into
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, merge_into, None, None, None, None)
        self.assertRaises(ValueError, merge_into, [1], [2], -1, -1)
        a = [1, 2, 3]
        self.assertEqual(merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1, 2, 3]
        self.assertEqual(merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1, 3, 5, 7, 9, None, None, None]
        b = [4, 5, 6]
        expected = [1, 3, 4, 5, 5, 6, 7, 9]
        self.assertEqual(merge_into(a, b, 5, len(b)), expected)
