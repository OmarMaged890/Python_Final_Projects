from person_class import Person
class Nurse(Person):
    
    def __init__(self, name, age):
        super().__init__(name, age)  # Inherit name and age from Person 

    def view_info(self):
        """View information specific to the nurse."""
        base_info = super().view_info()
        return f"Nurse name{base_info}"