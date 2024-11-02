from person_class import Person
# Patient class inheriting from Person  
class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)  # Inherit name and age from Person
        self.ailment = ailment 

    def view_info(self):
        """View information specific to the patient."""
        base_info = super().view_info()
        return f"Patient Name{base_info}, Ailment: {self.ailment}"