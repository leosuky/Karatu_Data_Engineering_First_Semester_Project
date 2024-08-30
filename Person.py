
class Person:
    """
    Person(name: str, id_number: int)

    Creates a new person object

    Attributes:
            - name (str)
            - id_number (int}
    """

    def __init__(self, name: str, id_number: int) -> None:
        self.name = name
        self.id_number = id_number


    def __str__(self) -> str:
        return f"Name: {self.name}, id_number: {self.id_number}"