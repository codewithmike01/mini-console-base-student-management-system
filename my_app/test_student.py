import unittest
from lib.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        Student.intsantiate_students_from_file()
        self.id = '45'
        self.name = 'Test man'
        self.age = 23
        self.mentor = 'Roseline Bunks'
        self.major = 'Computer Science'


    def test_insert_student(self):
        self.result = Student.insert_student(self.id, self.name, self.age, self.mentor, self.major)
        self.assertEqual(self.result['message'],"Student Created Successfully!")

    def test_update_student(self):

        result = Student.update_student(self.id, self.name, 90, self.mentor, self.major)
        self.assertEqual(result['message'],"Student Updated Successfully!" )

    def test_y_delete_student(self):
        result = Student.delete_student(self.id)
        self.assertEqual(result['message'], "Student Deleted Successfully!" )

    def test_z_is_valid_id(self): # id does not exist
        result = Student.is_valid_id(self.id)
        self.assertFalse(result)


if __name__  ==  "__main__" :
    unittest.main()