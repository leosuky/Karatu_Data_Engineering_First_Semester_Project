from typing import Self, Union

from Course import Course
from Enrollment import Enrollment
from Insrtuctor import Instructor
from Student import Student


class StudentManagementSystem():
    """
    StudentManagementSystem( school_name: str )

    Creates a new Student Management Object

    Attributes:
            - school_name (str)
            - current_id (int)
            - students (dict)
            - instructors (dict)
            - courses (dict)
            - enrollments (dict)

    Methods:
            - add_student(self, name: str, major: str) -> Self
            - remove_student(self, student_id: int) -> Self
            - update_student(self, student_id: int, name: str=None, major: str=None) -> Self
            - add_instructor(self, name: str, department: str) -> Self
            - remove_instructor(self, instructor_id: int) -> Self
            - update_instructor(self, instructor_id: int, name: str=None, department: str=None) -> Self
            - add_course(self, course_name: str) -> Self
            - remove_course(self, course_id: int) -> Self
            - update_course(self, course_id: int, course_name: str=None) -> Self
            - enroll_student(self, student_id: int, course_id: int) -> Self
            - uneroll_student(self, student_id: int, course_id: int) -> Self
            - assign_grade(self, student_id: int, course_id: int, grade: str) -> Self
            - retrieve_all_students_for_course(self, course_id: int) -> list
            - retireve_all_courses_for_student(self, student_id: int) -> Union[list, str]

    """

    def __init__(self, school_name: str) -> None:
        self.school_name = school_name
        self.current_id = 0
        self.students: dict = {}
        self.instructors: dict = {}
        self.courses: dict = {}
        self.enrollments: dict = {}


    def add_student(self, name: str, major: str) -> Self:
        """
        Creates a new Student object and adds it 
        to the Student Management System

        """
        self.current_id += 1
        self.students[self.current_id] = [Student(
            name=name,
            id_number=self.current_id,
            major=major
        ), []]
        return self
    

    def remove_student(self, student_id: int) -> Self:
        """
        Removes a student from the Student Management System

        Raises KeyError if the student_id IS NOT found 
        """
        if student_id in self.students:
            student_courses = self.students[student_id][1]
            if len(student_courses) > 0: # if the student is enrolled in any courses, unenroll before removing the student
                for course in student_courses:
                    self.uneroll_student(student_id, course.course_id)
            self.students.pop(student_id)
            return self
        else:
            raise KeyError(f"Student ID {student_id} does not exist")
        
    
    def update_student(self, student_id: int, name: str=None, major: str=None) -> Self:
        """
        Updates a student in the Student management System

        Raises KeyError if student_id IS NOT found
        """

        if student_id in self.students:
            student_to_update = self.students[student_id] # retrieve the student instance to update
            update_name = name if name is not None else student_to_update[0].name # only update the name if it was provided
            update_major = major if major is not None else student_to_update[0].major # only update the major if it was provided

            self.students[student_id][0] = Student(
                name=update_name,
                id_number=student_id,
                major=update_major
            )

            return self
        else:
            raise KeyError(f"Student ID {student_id} does not exist")
        

    def add_instructor(self, name: str, department: str) -> Self:
        """
        Creates a new Instructor object and adds it 
        to the Student Management System

        """
        self.current_id += 1
        self.instructors[self.current_id] = Instructor(
            name=name,
            id_number=self.current_id,
            department=department
        )
        return self
    

    def remove_instructor(self, instructor_id: int) -> Self:
        """
        Removes an instructor from the Student Management System

        Raises KeyError if the instructor_id IS NOT found 
        """
        if instructor_id in self.instructors:
            self.instructors.pop(instructor_id)
            return self
        else:
            raise KeyError(f"Instructor ID {instructor_id} does not exist")
        

    def update_instructor(self, instructor_id: int, name: str=None, department: str=None) -> Self:
        """
        Updates a instructor in the Student management System

        Raises KeyError if instructor_id IS NOT found
        """

        if instructor_id in self.instructors:
            instructor_to_update = self.instructors[instructor_id] # retrieve the instructor instance to update
            update_name = name if name is not None else instructor_to_update.name # only update the name if it was provided
            update_department = department if department is not None else instructor_to_update.department # only update the department if it was provided

            self.instructors[instructor_id] = Instructor(
                name=update_name,
                id_number=instructor_id,
                department=update_department
            )

            return self
        else:
            raise KeyError(f"Instructor ID {instructor_id} does not exist")
        
    def add_course(self, course_name: str) -> Self:
        """
        Creates a new Course object and adds it 
        to the Student Management System

        """
        self.current_id += 1
        self.courses[self.current_id] = Course(
            course_name=course_name,
            course_id=self.current_id
        )
        return self
    
    def remove_course(self, course_id: int) -> Self:
        """
        Removes a course from the Student Management System

        Raises KeyError if the course_id IS NOT found 
        """
        if course_id in self.courses:
            self.courses.pop(course_id)
            return self
        else:
            raise KeyError(f"Course ID {course_id} does not exist")
        
    def update_course(self, course_id: int, course_name: str=None) -> Self:
        """
        Updates a course in the Student management System

        Raises KeyError if course_id IS NOT found
        """

        if course_id in self.courses:
            course_to_update = self.courses[course_id] # retrieve the course instanace to update
            update_coursename = course_name if course_name is not None else course_to_update.course_name # only update the course name if it was provided

            self.courses[course_id] = Course(
                course_name=update_coursename,
                course_id=course_id,
                enrolled_students=course_to_update.enrolled_students
            )

            return self
        else:
            raise KeyError(f"Course ID {course_id} does not exist")
        

    def enroll_student(self, student_id: int, course_id: int) -> Self:
        """
        Enrolls a Student in a Course and stores the enrollment
        in the Student Management System

        Raises KeyError if course_id or student_id IS NOT found
        """
        if student_id in self.students:
            if course_id in self.courses:
                course = self.courses[course_id]
                student = self.students[student_id][0]

                enrollment_id = f'{student_id}-{course_id}' # custom enrollment id
                course.add_student(student) #add the student to the course
                self.enrollments[enrollment_id] = Enrollment(student=student, course=course) # keep track of all enrollments with unique enrollment ID
                self.students[student_id][1].append(course) # keeps track of courses enrolled by student

                return self
            else:
                return KeyError(f"Course ID {course_id} does not exist")
        else:
            KeyError(f"Student ID {student_id} does not exist")

    def uneroll_student(self, student_id: int, course_id: int) -> Self:
        """
        Removes a student's enrollment in a course.

        Raises KeyError if no enrollment found
        """

        enrollment_id = f'{student_id}-{course_id}' # custom enrollment ID
        if enrollment_id in self.enrollments:
            course = self.courses[course_id]
            student = self.students[student_id][0]

            course.remove_student(student)
            self.enrollments.pop(enrollment_id)
            self.students[student_id][1].remove(course)

            return self
        else:
            raise KeyError(f"No enrollment found for student ID {student_id} for course ID {course_id}")
        
    def assign_grade(self, student_id: int, course_id: int, grade: str) -> Self:
        """
        Assigns the grade for a students enrollment

        Raises KeyError if no enrollment found
        """

        enrollment_id = f'{student_id}-{course_id}' # custom enrollment ID
        if enrollment_id in self.enrollments:
            self.enrollments[enrollment_id].assign_grade(grade)
            return self
        else:
            raise KeyError(f"No enrollment found for student ID {student_id} for course ID {course_id}")
        
    def retrieve_all_students_for_course(self, course_id: int) -> list:
        """
        Retrives all the students enrolled in a specific course.

        Returns:
        - list of enrolled students

        Raises:
        - KeyError if course id is NOT found
        """

        if course_id in self.courses:
            return self.courses[course_id].enrolled_students
        else:
            raise KeyError(f"Course ID {course_id} does not exist")
        
    def retireve_all_courses_for_student(self, student_id: int) -> Union[list, str]:
        """
        Retrieves all courses a student is enrolled in.

        Returns:
        - list of enrolled courses
        - string response if no courses

        Raises:
        - KeyError if student_id is NOT found.
        """

        if student_id in self.students:
            courses = self.students[student_id][1]
            if len(courses) == 0:
                return "Student Not enrolled in any courses"
            else:
                return courses
            
        else:
            raise KeyError(f"Student ID {student_id} does not exist")
        

    def __str__(self) -> str:
        return f"""
                {self.school_name} Student Management System

                Total Number of Students: {len(self.students)}
                
                Total Number of Instructors: {len(self.instructors)}
                
                Total Number of Courses: {len(self.courses)}
                
                Total Number of Enrollments: {len(self.enrollments)}
                """


