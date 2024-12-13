from model import StudentGrades

class GradeControl:
    """Handle the model and view"""
    def __init__(self, scores):
        self.student_grades = StudentGrades(scores)

    def get_grades(self):
        """Return a list of tuples with student number, score, and grade"""
        return [(idx + 1, score, self.student_grades.get_grade(score))
            for idx, score in enumerate(self.student_grades.scores)]

    def get_avg_and_grade(self):
        """Return the average score and its grade"""
        avg = self.student_grades.cal_avg()
        avg_grade = self.student_grades.get_grade(avg)
        return avg, avg_grade