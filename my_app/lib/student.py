import csv
from lib.person import Person

class Student(Person):
    all_student = []

    def __init__(self, id, name, age, major, mentor ) -> None:
         super().__init__(id, name, age, major)
         self.mentor = mentor

    def accept_initial_input():
        id = str(input('Enter Student Id () : '))

        if Student.is_valid_id(id):
            print("""
            Id is taken, Use a different Id
            """)
            Student.accept_initial_input()

        name = str(input('Enter Student name: '))
        age = int(input('Enter Student age: '))
        mentor = str(input('Enter Student mentor: '))
        major = str(input('Enter Student major: '))

        return id, name, age, mentor, major


    def accept_update_input():
        name = str(input('Enter Student name: '))
        age = int(input('Enter Student age: '))
        mentor = str(input('Enter Student mentor: '))
        major = str(input('Enter Student major: '))

        return  name, age, mentor, major


    def insert_student():
        """
        Accept Student details..

        Attribute: name is (str), age(int),
        mentor(str), major(str)
        """

        id, name, age, mentor, major = Student.accept_initial_input()
        Student.save_student_details_csv_file(id, name, age, mentor, major)
        print("""

        === Student Details Saved Sucessfully!!! ===
        """)

    def update_student():

        """Accept Student Id.

        Use stude id to map student and
        update student detail

        Attribute: Id is str
        """

        id = str(input('Enter Student selected Id: '))

        if Student.is_valid_id(id):
            name, age, mentor, major = Student.accept_update_input()

            def get_update(student): # Map callback function

                if student['id'] == id:
                    student['name'] = name
                    student['age'] = age
                    student['mentor'] = mentor
                    student['major'] = major
                    student['obj'] = Student(id, name, age, mentor, major)
                    return student
                return student


            students_list = map(get_update,Student.all_student)
            Student.write_to_csv_file(students_list)
            print("""

            === Student Details Updated Sucessfully!!! ===
            """)

        else: # No valid Id
            print("""
            Id not found in record

            """)

    def delete_student():
        """Accept Student Id.

        Use student id to filter student and
        delete student detail

        Attribute: Id is str
        """
        id = str(input('Enter Student selected Id: '))

        if Student.is_valid_id(id):

            def filtered_students(student): # Filter Callback Function
                if (student['id'] != id):
                    return student

            new_students = filter(filtered_students,Student.all_student)
            Student.write_to_csv_file(new_students)
            print("""

            === Student Details Deleted Sucessfully!!! ===
            """)

        else: # No valid Id
            print("""
            Id not found in record

            """)



    def save_student_details_csv_file(id, name, age, mentor, major):
        with open("./data/students.csv",'a', newline='') as student:
            student_writer = csv.writer(student)
            student_writer.writerow([id, name, age, mentor, major])


    def write_to_csv_file(new_student_list):
        with open('./data/students.csv', 'w', newline='') as student:
                    for student_list in new_student_list:

                        student_writer = csv.writer(student)
                        student_writer.writerow([
                            student_list['id'],
                            student_list['name'],
                            student_list['age'],
                            student_list['mentor'],
                            student_list['major'],
                        ])




    def is_valid_id(id):
        for student in Student.all_student:
            if id == student['id']:
                return True
        return False

    @classmethod
    def display_students(cls):
         print('Students display')
         for student in cls.all_student:

              print(Student.__repr__(student['obj']))


    @classmethod
    def intsantiate_students_from_file(cls):
        """Display all students in the csv file.


        Operation: All students are loaded into
        class property all_student in array of objects

        Attribute: id (str), major (str), mentor (str),
          name (str), age (int)
        """

        student_obj = {}
        students_list = []

        with open("./data/students.csv", "r") as students:

            for student in students:
                student_list = student.strip().split(',')

                student_obj['id'] = student_list[0].strip()
                student_obj['name'] =   student_list[1].strip()
                student_obj['age'] =   student_list[2].strip()
                student_obj['mentor'] =   student_list[3].strip()
                student_obj['major'] =   student_list[4].strip()

                students_list.append(student_obj)
                student_obj = {}

            cls.__instantiate_students(students_list)


    @classmethod
    def __instantiate_students(cls, students):

          cls.all_student = []

          for student in students:
              student['obj'] = Student(
                   student['id'],
                   student['name'],
                   student['age'],
                   student['major'],
                   student['mentor'])
              cls.all_student.append(student)



    def __repr__(self):

            return f"""
    Id: {self.id}
    Name: {self.name}
    Age: {self.age}
    Major: {self.major}
    Mentor: {self.mentor}

    ======================
            """


