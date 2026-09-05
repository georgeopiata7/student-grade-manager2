students_result = {}

def add_student():
    try:
        student_name = input("Enter student's NAME: ")
        student_marks = int(input("Enter student's MARKS: "))
        students_result[student_name] = student_marks
        print(f"{student_name} added successfully!")
    except ValueError:
        print(f"INVALID INPUT")

def view_result():
    if len(students_result.items()) == 0:
        print(f"NO STUDENT FOUND")
    else:
        for student_name, student_marks in students_result.items():
            print(f"{student_name}: {student_marks}%")                                

def highest_student():
    if len(students_result.items()) == 0:
        print(f"NO STUDENT FOUND")
    else:
        highest_score = max(students_result.values())
        print(f"Highest-score = {highest_score}%")

def lowest_score():
    if len(students_result.items()) == 0:
            print(f"NO STUDENT FOUND")
    else:
        lowest_score = min(students_result.values())
        print(f"Lowest-score = {lowest_score}%")

def students_average():
    if len(students_result.items()) == 0:
            print(f"NO STUDENT FOUND")
    else:        
        total_marks = sum(students_result.values())
        total_students = len(students_result)
        average = total_marks / total_students
        print(f"Average = {average}%")






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
            lowest_score()
        elif user_option == 5:
            students_average()
        elif user_option == 6:
            print(f"Exited successfully!")
            break
        else:
            print(f"Invalid choice")
        continue
    except ValueError:
        print(f"INVALID CHOICE!")
        continue