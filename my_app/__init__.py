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


def insert_student():
    """
    Accept Student details

    Attribute: name is (str), age(int), 
    mentor(str), major(str)
    """
    pass

def delete_student():
      """
    Accept Student Id 

    Use student id to filter student and 
    delete student detail

    Attribute: Id is str
    """
    pass


def main():
    
    display_options()

    option: str = str(input('Select an Option: '))
    print(option)



main()