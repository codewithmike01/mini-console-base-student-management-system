
from lib.student import Student, Person


def display_options():
    print("""
    1. Display all students
    2. Update Student detail
    3. insert new Student detail
    4. Delete a Student detail
    5. Exist
    """)


def switch_option(opt):
    """
    switch_option controls the routing of options,
    and calling the expected function.

    """
    if opt == '1':
        Student.display_students()

    elif opt == '2':
        Student.accept_update_input()

    elif opt == '3':
        Student.accept_initial_input()

    elif opt == '4':
        Student.accept_delete_input()

    elif opt == '5':
        Person.keyboard_interrupt_handler()


def main():
    Student.intsantiate_students_from_file()

    print('=========== Options ============')

    display_options()

    try: #Exception Handled For Keyboard Interrupt

        option: str = str(input('Select an Option: '))

    except KeyboardInterrupt:
        Person.keyboard_interrupt_handler()

    while option != 5:
        switch_option(option)
        main()




main() # Main Calling point