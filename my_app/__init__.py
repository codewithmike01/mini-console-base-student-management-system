import csv
from lib.student import Student

def display_options():
    print("""
    1. Display all students
    2. Update Student detail
    3. insert new Student detail
    4. Delete a Student detail
    5. Exist
    """)

def accept_update_input():
    name = str(input('Enter Student name: '))
    age = int(input('Enter Student age: '))
    mentor = str(input('Enter Student mentor: '))
    major = str(input('Enter Student major: '))

    return  name, age, mentor, major


def accept_initial_input():
    id = str(input('Enter Student Id () : '))

    if valid_id_avialability(id):
        print("""
        Id is taken, Use a different Id
        """)
        insert_student()

    name = str(input('Enter Student name: '))
    age = int(input('Enter Student age: '))
    mentor = str(input('Enter Student mentor: '))
    major = str(input('Enter Student major: '))

    return id, name, age, mentor, major





def select_id():
    id = str(input('Enter Student Id to update: '))
    return id

def valid_id_avialability(id):

    for student in Student.all_student:
        if id == student['id']:
            return True
    return False


def intsantiate_students_from_file():
    """Display all students in the csv file.
    """

    student_obj = {}
    students_list = []
    with open("students.csv", "r") as students:

        for student in students:
            student_list = student.strip().split(',')

            student_obj['id'] = student_list[0].strip()
            student_obj['name'] =   student_list[1].strip()
            student_obj['age'] =   student_list[2].strip()
            student_obj['mentor'] =   student_list[3].strip()
            student_obj['major'] =   student_list[4].strip()

            students_list.append(student_obj)
            student_obj = {}

        Student.instantiate_students(students_list)

def update_student():

    """Accept Student Id.

    Use stude id to map student and
    update student detail

    Attribute: Id is str
    """


    id = select_id()

    if valid_id_avialability(id):
        name, age, mentor, major = accept_update_input()
        def get_update(student):

            if student['id'] == id:
                student['name'] = name
                student['age'] = age
                student['mentor'] = mentor
                student['major'] = major
                student['obj'] = Student(id, name, age, mentor, major)
                return student
            return student

        if len(Student.all_student) > 0:
            students_list = map(get_update,Student.all_student)

            with open('students.csv', 'w', newline='') as student:
                for student_list in students_list:
                    student_list['obj'] = Student(
                         student_list['id'],
                         student_list['name'],
                         student_list['age'],
                         student_list['mentor'],
                         student_list['major']
                    )

                    student_writer = csv.writer(student)
                    student_writer.writerow([
                        student_list['id'],
                        student_list['name'],
                        student_list['age'],
                        student_list['mentor'],
                        student_list['major'],
                       ])
        else:
            print('')
            print('No student record found!!!')

    else:
        print("""
        Id not found in record

        """)
        main()




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
    Accept Student details..

    Attribute: name is (str), age(int),
    mentor(str), major(str)
    """

    id, name, age, mentor, major = accept_initial_input()
    validate_student_detail(id, name, age, mentor, major)


    instantiate_student(id, name, age, mentor, major)
    save_student_detail(id, name, age, mentor, major)
    print("""

    === Student Details Saved Sucessfully!!! ===
    """)









def delete_student():
    """Accept Student Id.

    Use student id to filter student and
    delete student detail

    Attribute: Id is str
    """
    pass

def switch_option(opt):
    if opt == '1':
        Student.display_students()

    elif opt == '2':
        update_student()

    elif opt == '3':
        insert_student()

    elif opt == '4':
        delete_student()

    elif opt == '5':
        return exit()







def main():

    intsantiate_students_from_file()


    print(' ======Options=====')
    display_options()

    option: str = str(input('Select an Option: '))

    while option != 5:
        switch_option(option)
        main()


main()