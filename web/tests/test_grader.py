import unittest
import argparse
import sys
import os
# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from upload.grader import grade_question, calculate_score
class TestGrade(unittest.TestCase):
    def test_grade_question(self):
        answer_key = ["A", "B", "C", "D"]
        student_answers = ["A", "B", "D", "D"]
        self.assertTrue(grade_question(answer_key, student_answers, 0))
        self.assertTrue(grade_question(answer_key, student_answers, 1))
        self.assertFalse(grade_question(answer_key, student_answers, 2))
        self.assertTrue(grade_question(answer_key, student_answers, 3))
    def test_calculate_score(self):
        answer_key = ["A", "B", "C", "D"]
        student_answers = ["A", "B", "D", "D"]
        self.assertEqual(calculate_score(answer_key, student_answers), 3)
  
if __name__ == "__main__":
    unittest.main()