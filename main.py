import Student_Management_System


if __name__ == "__main__":
    Altschool = Student_Management_System.StudentManagementSystem("Altschool Africa")

    print(Altschool)

    print('adding 1 student...')
    Altschool.add_student(name='Sunkanmi', major='Data Engineering')

    print(Altschool.students[1][0])
    print(" ")

    print("adding 2 more students...")
    Altschool.add_student('Tabitha', 'Physics').add_student('Fatima', 'Geography')

    # Print all students in the SMS
    for i in Altschool.students.keys():
        print(Altschool.students[i][0])

    print(" ")

    print('Adding 2 instructors and removing student with ID 2 ')
    Altschool.add_instructor('Charles', 'Psycology').add_instructor('Kevin', 'Geography').remove_student(2)

    # Print all students in the SMS
    for i in Altschool.students.keys():
        print(Altschool.students[i][0])

    print(" ")

    # Print all instructors in the SMS
    for i in Altschool.instructors.keys():
        print(Altschool.instructors[i])

    print(" ")

    print("Adding 3 courses to Altschool")
    Altschool.add_course("Geography").add_course("Mechanical Engineering").add_course("Mathematics")

    # print all courses in the SMS
    for i in Altschool.courses.keys():
        print(Altschool.courses[i])

    print(" ")

    print('Enrolling students')
    Altschool.enroll_student(1,6).enroll_student(1,7).enroll_student(3,8)

    # print all enrollments
    for i in Altschool.enrollments.keys():
        print(Altschool.enrollments[i])

    print(" ")

    # print Altschool
    print(Altschool)

    print(" ")

    print("Students and courses enrolled")
    for i in Altschool.students.keys():
        print(f"{Altschool.students[i][0]}, Courses: {Altschool.students[i][1]}")

    print(" ")

    print('Getting all courses for Sunkanmi')
    courses_sunkanmi = Altschool.retireve_all_courses_for_student(1)
    for i in courses_sunkanmi:
        print(i)

    print(" ")

    print('Getting all courses for Fatima')
    courses_fatima = Altschool.retireve_all_courses_for_student(3)
    for i in courses_fatima:
        print(i)

    print(" ")

    print('Unenroll Sunkanmi from Geography and ennroll him in Mathematics')
    Altschool.enroll_student(1, 8).uneroll_student(1, 6)
    for i in Altschool.courses.keys():
        print(Altschool.courses[i])

    print(" ")

    print('Get all students enrolled in Mathematics')
    all_students_for_math = Altschool.retrieve_all_students_for_course(8)
    for i in all_students_for_math:
        print(i)

    print(" ")

    print('List of all current enrollments')
    for i,j in Altschool.enrollments.items():
        print(i, j)

    print(" ")

    print('Assiging Grades')
    Altschool.assign_grade(1, 7, 'A-').assign_grade(3, 8, 'C-').assign_grade(1, 8, 'A+')
    for i,j in Altschool.enrollments.items():
        print(i, j)

    print(" ")

    print("Remove Geography and Fatima from the Student management System")
    Altschool.remove_course(6).remove_student(3)

    print(" ")

    print('List of all current enrollments')
    for i,j in Altschool.enrollments.items():
        print(i, j)

    print(" ")

    print('List of all courses')
    for i in Altschool.courses.keys():
        print(Altschool.courses[i])

    print(" ")

    print(Altschool)

    print(" ")

    print('Sunkanmi is changing his major to Applied Statistics')
    Altschool.update_student(1, major='Applied Statistics')

    print(" ")

    for i in Altschool.students.keys():
        print(f"{Altschool.students[i][0]}, Courses: {Altschool.students[i][1]}")


    print(" ")
    print("THE END!")
