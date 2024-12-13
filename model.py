from typing import List

class StudentGrades:
    """Handles grade calculations"""

    def __init__(self, scores: List[int]):
        """Initialize the student scores and calculate the high score"""
        self.scores = scores
        self.high_score = max(scores)

    def get_grade(self, student_score: int) -> str:
        """Determine the letter grade based on score and the highest score."""
        if student_score >= self.high_score - 10:
            return 'A'
        elif self.high_score - 20 <= student_score < self.high_score - 10:
            return 'B'
        elif self.high_score - 30 <= student_score < self.high_score - 20:
            return 'C'
        elif self.high_score - 40 <= student_score < self.high_score - 30:
            return 'D'
        else:
            return 'F'

    def cal_avg(self) -> float:
        """Calculate the average score of all students"""
        return sum(self.scores) / len(self.scores)
