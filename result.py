students_result = {}

def add_student():
    
    try:
        student_name = input("Enter student's NAME: ")
        if student_name in students_result:
            print(f"STUDENT ALREADY EXIST")
            return
        
        student_marks = int(input("Enter student's MARKS: "))
        if student_marks >= 0 and student_marks <= 100:
            students_result[student_name] = student_marks
            print(f"{student_name} added successfully!")
        else:
            print(f"ENTER VALID MARKS")
            
        
    except ValueError:
        print(f"INVALID INPUT")

def view_result():
    if not students_result:
        print(f"NO STUDENT FOUND")
    else:
        for student_name, student_marks in students_result.items():
            grades = add_grades(student_marks)
            print(f"{student_name}: {student_marks}% - Grade:{grades}")                                

def highest_student():
    if not students_result:
        print(f"NO STUDENT FOUND")
    else:
        highest_student = max(students_result, key = students_result.get)
        highest_marks = max(students_result.values())

        print(f"Highest-student = {highest_student} : {highest_marks}%")

def lowest_student():
    if not students_result:
            print(f"NO STUDENT FOUND")
    else:
        lowest_student = min(students_result, key = students_result.get)
        lowest_marks = min(students_result.values())
        print(f"Lowest-student = {lowest_student} : {lowest_marks}%")

def students_average():
    if not students_result:
            print(f"NO STUDENT FOUND")
    else:        
        total_marks = sum(students_result.values())
        total_students = len(students_result)
        average = total_marks / total_students
        print(f"Average = {average}%")



def add_grades(student_marks):
    if student_marks >= 80 and student_marks <= 100:
        return "A"
    elif student_marks >= 70 and student_marks <= 79:
        return "B"
    elif student_marks >= 60 and student_marks <= 69:
        return "C"
    elif student_marks >= 50 and student_marks <=59:
        return "D"
    elif student_marks >= 0 and student_marks <= 49:
        return "E"






while True:
    print(f"MAKE A CHOICE FROM THE LIST BELOW.")
    print(f"1. Add student ")
    print(f"2. View students' result ")
    print(f"3. Show the highest student ")
    print(f"4. Show the lowest student ")
    print(f"5. Calculate average of students ")
    print(f"6. Exit")


    try:
        user_option = int(input("Enter CHOICE: "))
        if user_option not in [1, 2, 3, 4, 5, 6]:
            print(f"INVALID OPTION")
            
        
        elif user_option == 1:
            add_student()

        elif user_option == 2:
            view_result()

        elif user_option == 3:
            highest_student()

        elif user_option == 4:
            lowest_student()
        elif user_option == 5:
            students_average()
        elif user_option == 6:
            print(f"Exited successfully!")
            break
        
        
    except ValueError:
        print(f"INVALID CHOICE!")
