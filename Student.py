from Person import Person

class Student(Person):
    """
    Student(name: str, id_number: int, major: str)

    Inherits from base Person class and creates a new student object
    
    Attributes:
            - name (str)
            - id_number (int}
            - major (str)
    """

    def __init__(self, name: str, id_number: int, major: str) -> None:
        super().__init__(name, id_number)
        self.major = major

    def __str__(self) -> str:
        return f"{super().__str__()}, Major: {self.major}"