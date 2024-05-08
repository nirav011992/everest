import unittest
from outcome_chart import get_commentary

class TestGetCommentary(unittest.TestCase):
    def test_get_commentary(self):
        self.assertEqual(get_commentary("wicket"), "It's a wicket. Excellent line and length.")
        self.assertEqual(get_commentary("6 runs"), "That's massive and out of the ground.")
        self.assertEqual(get_commentary("4 runs"), "Just over the fielder.")
        self.assertEqual(get_commentary("1 run"), "Excellent running between the wickets.")
        self.assertEqual(get_commentary("2 runs"), "Convert ones into twos.")
        self.assertEqual(get_commentary("0 runs"), "Edged and taken.")
        self.assertEqual(get_commentary("unknown outcome"), "Excellent shot.")

if __name__ == '__main__':
    unittest.main()