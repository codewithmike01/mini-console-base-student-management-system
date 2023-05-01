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
    pass

def update_student():
    
    """
    Accept Student Id 

    Use stude id to map student and 
    update student detail

    Attribute: Id is str
    """
    pass


def validate_student_detail(name, age, mentor, major):
    # Validation
    assert isinstance(name, str), "name must be string"
    assert isinstance(age, int), "age must be integer"
    assert isinstance(mentor, str), "mentor must be string"
    assert isinstance(major, str), "major must be string"

def instantiate_student(name, age, mentor, major):
    # Create instance of Student Class
    Student(name, age, mentor, major)

def save_student_detail(name, age, mentor, major):
    with open("students.csv",'a', newline='') as student:
        student_writer = csv.writer(student)
        student_writer.writerow([name, age, mentor, major])

def insert_student():
    """
    Accept Student details

    Attribute: name is (str), age(int), 
    mentor(str), major(str)
    """
     
    name = str(input('Enter Student name: '))
    age = int(input('Enter Student age: '))
    mentor = str(input('Enter Student mentor: '))
    major = str(input('Enter Student major: '))

    validate_student_detail(name, age, mentor, major )
    instantiate_student(name, age, mentor, major)
    save_student_detail(name, age, mentor, major)
   

    
    

  

def delete_student():
    """
    Accept Student Id 

    Use student id to filter student and 
    delete student detail

    Attribute: Id is str
    """
    pass

def switch_option(opt):
    
    #  1. Display all students
    # 2. Update Student detail
    # 3. insert new Student detail
    # 4. Delete a Student detail

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