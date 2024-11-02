from person_class import Person

# Doctor class inheriting from Person
class Doctor(Person):
    
    def __init__(self, name, age, specialty):
        super().__init__(name, age)  # Inherit name and age from Person
        self.specialty = specialty

    def view_info(self):
        """View information specific to the doctor."""
        base_info = super().view_info()
        return f"Doctor name{base_info}, Specialty: {self.specialty}" 
# Nurse class inheriting from Person