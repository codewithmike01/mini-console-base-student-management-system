import csv
from lib.person import Person


class Student(Person):
    all_student = []

    def __init__(self, id: str, name: str, age: int, major: str, mentor: str ) -> None:
         super().__init__(id, name, age, major)
         self.mentor = mentor


    @staticmethod
    def accept_delete_input():
         """
         accept_delete_input process delete students insert value.

         No Parameters
         """
         try:
              id = str(input('Enter Student selected Id: '))
              Student.delete_student(id)
              print("""

                === Student Details Deleted Sucessfully!!! ===
                """)

         except KeyboardInterrupt:
              Student.keyboard_interrupt_handler()

    @staticmethod
    def accept_initial_input():
        """
        accept_initial_input process students insert values.

        No Parameters
        """

        try: # Handle Exception KeyboardInterrupt
             id = str(input('Enter Student Id () : '))

             if Student.is_valid_id(id): # Check of ID Already exist
                 print("""
                Id is taken, Use a different Id
                """)
                 Student.accept_initial_input()

             name = str(input('Enter Student name: '))

             try: # Handle Exception ValueError & KeyboardInterrupt
                 age = int(input('Enter Student age: '))
                 mentor = str(input('Enter Student mentor: '))
                 major = str(input('Enter Student major: '))
                 Student.insert_student(id, name, age, major, mentor)

                 print("""

                    === Student Details Saved Sucessfully!!! ===
                    """)

             except ValueError:
                 print("""

                ====== You should enter number(s) for age ======

                """)

                 Student.accept_initial_input()

             except KeyboardInterrupt:
                 Student.keyboard_interrupt_handler()

        except KeyboardInterrupt:
             Student.keyboard_interrupt_handler()

    @staticmethod
    def accept_update_input():
        """
        accept_update_input process students update values.

        No Parameters
        """

        try: # Handle Exception KeyboardInterrupt
             id = str(input('Enter Student selected Id: '))

             try:
                 name = str(input('Enter Student name: '))
                 age = int(input('Enter Student age: '))
                 mentor = str(input('Enter Student mentor: '))
                 major = str(input('Enter Student major: '))

                 Student.update_student(id, name, age, major, mentor )

                 print("""

                    === Student Details Updated Sucessfully!!! ===
                    """)

             except ValueError:
                 print("""

                ====== You should enter number(s) for age ======

                """)

                 Student.accept_update_input()

             except KeyboardInterrupt:
                 Student.keyboard_interrupt_handler()

        except KeyboardInterrupt:
             Student.keyboard_interrupt_handler()

    @classmethod
    def insert_student(cls, id: str, name: str, age: int, mentor: str, major: str):
        """
        insert_student.

        Attribute: id: str, name: str ,
        age: int, mentor: str, major: str
        """

        Student.save_student_details_csv_file(id, name, age, mentor, major)

        return {"status": 200, "message": "Student Created Successfully!"} # To mimic a response from server

    @classmethod
    def update_student(cls, id: str, name: str, age: int, mentor: str, major: str):
        """update_student.

        Use student id to map students list and
        update student detail

        Attribute: id: str, name: str ,
        age: int, mentor: str, major: str
        """

        if Student.is_valid_id(id):

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

                return {"status": 200, "message":"Student Updated Successfully!"} # To mimic a response from server

        else: # No valid Id
            print("""
            Id not found in record

            """)

    @classmethod
    def delete_student(cls, id: str):
        """
        delete_student Use student id to filter student and
        delete student detail.

        Attribute: id is str
        """

        if Student.is_valid_id(id):

            def filtered_students(student): # Filter Callback Function
                if (student['id'] != id):
                    return student

            new_students = filter(filtered_students,Student.all_student)
            Student.write_to_csv_file(new_students)

            return {"status":200, "message" : "Student Deleted Successfully!"}

        else: # No valid Id
            print("""
            Id not found in record

            """)

    def save_student_details_csv_file(id: str, name: str, age: int, mentor: str, major: str):
        """
        save_student_details_csv_file into the csv file for students
        record, appending to the existing data.


        Attribute: id: str , name: str,
        age: int, major: str, mentor: str
        """
        with open("./data/students.csv",'a', newline='') as student:
            student_writer = csv.writer(student)
            student_writer.writerow([id, name, age, mentor, major])

    def write_to_csv_file(new_student_list: list):
        """
        write_to_csv_file writes into the csv file for students
        record and overriding previous data
        Accepts: Array of student object.

        Attribute: [{
          id , name, age, major, mentor
          }].
        """
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

    @staticmethod
    def is_valid_id(id: str):
        """
        is_valid_id checks if id is present in record returns true
        returns False if id does not exist in record.

        Attribute: id.
        """
        for student in Student.all_student:
            if id == student['id']:
                return True
        return False

    @classmethod
    def display_students(cls):
         """display_students
         displays all students in the record.

         """
         print(f"""
         ===== Display All {len(Student.all_student)} Students =====
         """)

         for index, student in enumerate(cls.all_student):

              print(Student.__repr__(student['obj'], index))

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
    def __instantiate_students(cls, students: list):
          """
          __instantaite_students class method
          helps to append student records in CSV file
          into the class property array
          called all_student and intstantiate all records.

          Attribute: all_student [{
          id , name, age, major, mentor
          }].
          """

          cls.all_student = []

          for student in students:
              student['obj'] = Student(
                   student['id'],
                   student['name'],
                   student['age'],
                   student['major'],
                   student['mentor'])
              cls.all_student.append(student)

    def __repr__(self, index):

            return f"""
            === ( {int(index) + 1 } ) ===
    Id: {self.id}
    Name: {self.name}
    Age: {self.age}
    Major: {self.major}
    Mentor: {self.mentor}

    ======================
            """


