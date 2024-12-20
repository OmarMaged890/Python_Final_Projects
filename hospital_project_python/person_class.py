class Person : 
    """Base class for all people in the hospital."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        """View basic information about the person."""
        return f" :{self.name}, Age: {self.age}"