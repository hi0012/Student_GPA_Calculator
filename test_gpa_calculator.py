import unittest

from gpa_calculator import calculate_gpa, grade_to_points


class TestGpaCalculator(unittest.TestCase):
    def test_grade_points(self):
        self.assertEqual(grade_to_points("A"), 4.0)
        self.assertEqual(grade_to_points("b+"), 3.3)
        self.assertEqual(grade_to_points(" F "), 0.0)

    def test_invalid_grade(self):
        with self.assertRaises(ValueError):
            grade_to_points("E")

    def test_unweighted_list(self):
        self.assertEqual(calculate_gpa(["A", "B", "C"]), 3.0)

    def test_credit_weighted(self):
        # (4.0*4 + 3.0*3) / 7 = 3.57
        self.assertEqual(calculate_gpa([("A", 4), ("B", 3)]), 3.57)

    def test_empty(self):
        self.assertEqual(calculate_gpa([]), 0.0)

    def test_invalid_credits(self):
        with self.assertRaises(ValueError):
            calculate_gpa([("A", 0)])


if __name__ == "__main__":
    unittest.main()
