

class Student:
    all_student = []

    def __init__(self, id: str, name: str, age: int, mentor: str, major: str):
        self.id = id
        self.name = name
        self.age = age
        self.mentor = mentor
        self.major = major


    @classmethod
    def instantiate_students(cls, students):
          cls.all_student = []
          for student in students:
              student_obj = cls(student['id'], student['name'], student['age'], student['mentor'], student['major'] )
              student['obj'] = student_obj

              cls.all_student.append(student)

          for student in cls.all_student:

              print(repr(student['obj']))


    def __repr__(self):

            return f"""
    Id: {self.id}
    Name: {self.name}
    Age: {self.age}
    Major: {self.major}
    Mentor: {self.mentor}

    ======================
            """


