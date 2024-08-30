from typing import Self
from Student import Student
from Course import Course


class Enrollment():
    """
    Enrollment( student: type[Student], course: type[Course] )

    creates a new Course object.

    Attributes:
            - student (type[Student])
            - course (type[Course])
            - grade (str)

    Methods:
            - assign_grade(grade) -> Self
    """

    def __init__(self, student: type[Student], course: type[Course]) -> None:
        self.student = student
        self.course = course
        self.grade: str = None


    def assign_grade(self, grade: str ) -> Self:
        """
        Assigns a grade to the current enrollment
        """

        self.grade = grade
        return self
    

    def __str__(self) -> str:
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade if self.grade is not None else 'Not assigned'}"