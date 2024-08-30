from typing import Self
from Student import Student

class Course():
    """
    Course( course_name: str, course_id: int )

    creates a new Course object.

    Attributes:
            - course_name (str)
            - course_id (int)
            - enrolled_students (list[type[Student]])

    Methods:
            - add_student(student) -> Self
            - remove_student(student) -> Self
    """

    def __init__(self, course_name: str, course_id: int, enrolled_students: list[type[Student]] = None) -> None:
        enrolled_students = [] if enrolled_students is None else None
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = enrolled_students

    def add_student(self, student: type[Student]) -> Self:
        """
        Adds a new Student object to list of enrolled students

        Raises TypeError if student IS NOT type[Student]
        """

        if isinstance(student, Student) == True:
            # Only append the student if the value provided is the correct type
            self.enrolled_students.append(student)
            return self
        else:
            raise TypeError("student must be of type Student.")
        

    def remove_student(self, student: type[Student]) -> Self:
        """
        Removes a student object from the list of enrolled students

        Raises TypeError if student IS NOT type[Student]
        """

        # Only remove the student if the value provided is the correct type and the student is enrolled
        if isinstance(student, Student) == True:
            if student in self.enrolled_students:
                self.enrolled_students.remove(student)
                return self
            else:
                print("The Student isn't enrolled in this Course")
                return self
        else:
            raise TypeError("student must be of type Student.")
        

    def __str__(self) -> str:
        return f" Course Name: {self.course_name}\n Course ID: {self.course_id}\n Enrolled Students: {self.enrolled_students}"
    