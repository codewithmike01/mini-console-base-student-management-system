
from lib.student import Student

def display_options():
    print("""
    1. Display all students
    2. Update Student detail
    3. insert new Student detail
    4. Delete a Student detail
    5. Exist
    """)


def switch_option(opt):
    if opt == '1':
        Student.display_students()

    elif opt == '2':
        Student.update_student()

    elif opt == '3':
        Student.insert_student()

    elif opt == '4':
        Student.delete_student()

    elif opt == '5':
        return exit()


def main():
    Student.intsantiate_students_from_file()

    print(' ======Options=====')

    display_options()

    option: str = str(input('Select an Option: '))

    while option != 5:
        switch_option(option)
        main()


# Main Calling point

main()