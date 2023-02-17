import os
import re

def add_student_info(students):
    
    num_of_students = int(input("Enter number of students: "))
    for i in range(num_of_students):
        student = {"student name": "", "student id": ""}

        student_name = input("Enter student name: ")
        while True:
            if re.match ("^[a-zA-Z ]+$", student_name):
                student["name"] = student_name
                break
            else:
                print("Xin moi nhap lai")
                student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        while True:
            if re.match ("BI\d{2}-\d{3}", student_id):
                student["id"] = student_id
                break
            else:
                print("ID khong hop le, xin moi nhap lai")
                student_id = input("Enter student ID: ")
        students.append(student) 
students = []

def add_course(courses):
    num_of_course = int(input("Enter number of courses: "))
    for i in range(num_of_course):
        course = {"course_name": "", "course_id": ""}
        
        course_name = input("Nhap ten khoa hoc: ")
        while True:
            if re.match ("^[a-zA-Z ]+$", course_name):
                break
            else:
                print("Ky tu khong hop le, xin moi nhap lai")
                course_name = input("Nhap ten khoa hoc: ")
        course_id = input("Nhap ma khoa hoc: ")
        while True:
            if re.match ("[A-Z.\d{3}]", course_id):
                break
            else:
                print("Ma so khong hop le, xin moi nhap lai")
                course_id = input("Nhap ma khoa hoc: ")
    courses.append(course)
courses = []

def add_mark(marks):
    mark = float(input("Nhap diem: "))
    while True:
        if mark > 0 or mark < 20:
            break
        else:
            print("Diem khong hop le, xin moi nhap lai")
            mark = input("Nhap diem: ")
marks = []

add_student_info(students)
add_course(courses)
add_mark(marks)

def show_student(students: list):
    for i in students:
        print(i["student name"], i["student id"])

def show_course(course: list):
    for i in course:
        print(i["course_name"], i["course_id"])

def user_selection(choice):
    print("-------------------")
    print("1. Show student info")
    print("2. Show course info")
    print("3. Show overall mark")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Student info: ", show_student(students))
    elif choice == "2":
        print("Course info: ", show_course(courses))
    elif choice == "3":
        print("Mark: ", marks)
    elif choice == "4":
        print("See you later")
choice = []
user_selection(choice)








