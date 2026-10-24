#STUDENT MANAGEMENT SYSTEM

student=[]
def add_student(name,age,grade):
    student.append((name,age,grade))

def show_student(name):
    for student_name, student_age, student_grade in student:
        if student_name == name:
            print(f"Name: {student_name}, Age: {student_age}, Grade: {student_grade}")
            return
    print("Student not found")

def delete_student(name):
    if name not in student:
        print("Student not found")
    else:
        student.remove(name)
        print("Student deleted successfully")

while True:
    print("\n==student management system==")
    print("1.add student")
    print("2.show student")
    print("3.delete student")
    print("4.exit")

    choice=int(input("enter your choices:"))

    if choice==1:
        name=input("enter the student name you want to add:")
        age=int(input("enter the student age:"))
        grade=input("enter the student marks:")
        add_student(name,age,grade)
        print("student added successfully!!!")

    elif choice==2:
        name=input("enter the student name you want to see:")
        show_student(name)
        print("student shows successfully!!!")

    elif choice==3:
        name=input("enter the student name you want to delete:")
        delete_student(name)
        
    elif choice==4:
        print("Thank you")
        break
    else:
        print("invalid choice")
        

