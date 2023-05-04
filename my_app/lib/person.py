class Person:

    def __init__(self, id: str,
                 name: str, age: int,
                 major: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    @classmethod
    def keyboard_interrupt_handler(cls):
        """
        keyboard_interrupt_handler is
        a Person class method thats enables
        gracefully exist of program.

        """
        print("""

        ======= Exist Program Gracefully!!! =======

            """)
        return exit()
