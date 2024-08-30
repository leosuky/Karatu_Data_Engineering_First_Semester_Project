from Person import Person

class Instructor(Person):
    """
    Instructor(name: str, id_number: int, department: str)

    Inherits from base Person class and creates a new instructor object

    Attributes:
            - name (str)
            - id_number (int}
            - department (str)
    """

    def __init__(self, name: str, id_number: int, department: str) -> None:
        super().__init__(name, id_number)
        self.department = department

    def __str__(self) -> str:
        return f"{super().__str__()}, Department: {self.department}"