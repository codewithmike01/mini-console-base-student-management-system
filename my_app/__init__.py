import csv
from lib.student import Student

def display_options():
    print(f"""
    1. Display all students
    2. Update Student detail
    3. insert new Student detail
    4. Delete a Student detail
    """)


def display_student():
    """
    Display all students in the csv file
    """
    student_obj = {}
    students_list = []
    with open("students.csv", "r") as students:
        
        for student in students:
            student_list = student.strip().split(',')

            student_obj['id'] = student_list[0]  
            student_obj['name'] =   student_list[1]    
            student_obj['age'] =   student_list[2]    
            student_obj['mentor'] =   student_list[3]    
            student_obj['major'] =   student_list[4]  
            
            students_list.append(student_obj)
            student_obj = {}
            
        Student.instantiate_students(students_list)

def update_student():
    
    """
    Accept Student Id 

    Use stude id to map student and 
    update student detail

    Attribute: Id is str
    """
    pass


def validate_student_detail(id, name, age, mentor, major):
    # Validation
    assert isinstance(id, str), "Id must be string"
    assert isinstance(name, str), "name must be string"
    assert isinstance(age, int), "age must be integer"
    assert isinstance(mentor, str), "mentor must be string"
    assert isinstance(major, str), "major must be string"

def instantiate_student(id, name, age, mentor, major):
    # Create instance of Student Class
    Student(id, name, age, mentor, major)

def save_student_detail(id, name, age, mentor, major):
    with open("students.csv",'a', newline='') as student:
        student_writer = csv.writer(student)
        student_writer.writerow([id, name, age, mentor, major])

def insert_student():
    """
    Accept Student details

    Attribute: name is (str), age(int), 
    mentor(str), major(str)
    """
    
    id = str(input('Enter Student Id: '))
    name = str(input('Enter Student name: '))
    age = int(input('Enter Student age: '))
    mentor = str(input('Enter Student mentor: '))
    major = str(input('Enter Student major: '))

    validate_student_detail(id, name, age, mentor, major)
    instantiate_student(id, name, age, mentor, major)
    save_student_detail(id, name, age, mentor, major)
   

    
    

  

def delete_student():
    """
    Accept Student Id 

    Use student id to filter student and 
    delete student detail

    Attribute: Id is str
    """
    pass

def switch_option(opt):
    if opt == '1':
        display_student()

    elif opt == '2':
        update_student()

    elif opt == '3':
        insert_student()

    elif opt == '4':
        delete_student()
    
    else:
        display_options()
  

            


def main():
    
    display_options()

    option: str = str(input('Select an Option: '))
    
    switch_option(option)


main()