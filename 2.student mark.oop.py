from pydoc import describe
import re

print()


class Course:
    def __init__(GPA):
        GPA.course_list = []

    def describe(GPA):
        number_of_courses = int(
            input("Enter number of courses you want to add: "))
        for i in range(number_of_courses):
            print(f" == Course {i+1} ==")
            # Entering course name
            course_name_input = input("Enter course name: ")
            while True:
                if re.match ("^[a-zA-Z ]+$", course_name_input):
                    break
                else:
                    print("Please re-enter")
                    course_name_input = input("Enter course name: ")

            # Entering course ID
            course_id_input = input("Enter course ID: ").upper()
            while True:
                if re.match ("[A-Z.\d{3}]", course_id_input):
                    break
                else:
                    print("Invalid ID, please re-enter")
                    course_id_input = input("Enter course ID: ").upper()

            # Adding inputted course name and ID to the list
            GPA.course_list += [{"course_name": course_name_input,
                                 "course_id": course_id_input}]

    def show_course(GPA):
        for each_course in GPA.course_list:
            for key, value in each_course.items():
                print(f"{key}: {value}", end=" | ")

    def get_course_list(GPA):
        return GPA.course_list


class Classroom:
    def __init__(self):
        self.student_list = []

    def describe(self):
        number_of_students = int(
            input("Enter number of students you want to add: "))

        for i in range(number_of_students):
            print(f" == Student {i+1} ==")

            # Entering student name
            student_name_input = input("Enter student name: ")
            while True:
                if re.match ("^[a-zA-Z ]+$", student_name_input):
                    break
                else:
                    print("Please re-enter")
                    student_name_input = input("Enter student name: ")

            # Entering student ID
            student_id_input = input("Enter student ID: ").upper()
            while True:
                if re.match ("BI\d{2}-\d{3}", student_id_input):
                    break
                else:
                    print("Invalid ID, please re-enter")
                    student_id_input = input("Enter student ID: ").upper()

            # Adding inputted student name and ID to the list
            self.student_list += [{"Student Name": student_name_input,
                                   "Student ID": student_id_input, "Courses": []}]

    def add_one_course_marks(self, courses_list):

        if len(self.student_list) == 0:
            print("There is no student in the class")
            return ""
        if len(courses_list) == 0:
            print("There is no course in the class")
            return ""

        student_id_input = input(
            "Enter student ID of the student you want to add course mark: ").upper()

        # check if the student ID is in the student list
        while True:
            for student in self.student_list:
                if student_id_input == student["Student ID"]:
                    break
            else:
                print("Invalid student ID")
                student_id_input = input(
                    "Enter student ID of the student you want to add course mark: ").upper()
                continue
            break

        course_id_input = input(
            "Enter course ID of the course you want to add mark: ").upper()

        # check if the course ID is in the course list
        while True:
            for course in courses_list:
                if course_id_input == course["course_id"]:
                    break
            else:
                print("Invalid course ID")
                course_id_input = input(
                    "Enter course ID of the course you want to add mark: ").upper()
                continue
            break

        # att_mark, bonus, mid_term, final = input("Enter attendance mark, Bonus mid-term mark, final mark: ").split(" ")
        marks = input(
            "Enter attendance mark, Bonus, mid-term mark, final mark (separate by space): ").split(" ")
        while True:
            for mark in marks:
                if float(mark) >= 0 and float(mark) <= 20:
                    break
            else:
                print("Invalid mark")
                marks = input(
                    "Enter attendance mark, Bonus, mid-term mark, final mark (separate by space): ").split(" ")
                continue
            break

        att_mark, bonus, mid_term, final, = marks
        for student in self.student_list:
            if student_id_input == student["Student ID"]:
                student["Courses"] += [{"Course ID: ": course_id_input,
                                        "Attendance Mark: ": att_mark,
                                        "Bonus: ": bonus,
                                        "Midterm: ": mid_term,
                                        "Final": final,
                                        "GPA": float(att_mark)*10/100 + float(bonus)*10/100 + float(mid_term)*30/100 + float(final)*50/100}]
                break

    def add_multiple_course_marks(self, courses_list):
        number_of_students_to_add = int(input("Enter number of students you want to add course mark: "))
        for i in range(number_of_students_to_add):
            self.add_one_course_marks(courses_list)

    def print_student_list(self):
        for student in self.student_list:
            for key, value in student.items():
                print(f"{key}: {value}", end=" | ")
            print()


students = Classroom()
students.describe()

course = Course()
course.describe()
# course.show_course()

students.add_multiple_course_marks(course.get_course_list())

students.print_student_list()
